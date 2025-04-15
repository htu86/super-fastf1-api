from fastapi import HTTPException
from utils.sessionLoad import load_session
from utils.validateInput import validate_inputs

def get_circuit_info(year: int, gran_prix: str, session_type: str):
  validate_inputs(year, gran_prix , session_type )  

  try:
    race_session = load_session(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")

  circuit_data = race_session.get_circuit_info()
  circuit_corners = circuit_data.corners.to_dict("list") 
  circuits_rotation = circuit_data.rotation 
  marshall_sectors = circuit_data.marshal_sectors.to_dict("list")  
  marshall_lights = circuit_data.marshal_lights.to_dict("list")  

  if not circuit_corners or not circuits_rotation or not marshall_lights or not marshall_sectors:
    raise HTTPException(status_code=404, detail="Circuit data not found or no data available.")

  return {
    "corners": circuit_corners,
    "rotation": circuits_rotation,
    "marshall_sectors": marshall_sectors,
    "marshall_lights": marshall_lights
  }

def get_track_status_history(year: int, gran_prix: str, session_type: str):
  validate_inputs(year, gran_prix , session_type )    

  try:
    race_session = load_session(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")

  track_status_history = race_session.track_status.to_dict(orient="list")

  if not track_status_history:
    raise HTTPException(status_code=404, detail="Track status history data not found or no data available.")  

  return {
    "track_status_history": track_status_history
  }