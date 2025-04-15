from fastapi import HTTPException
from utils.sessionLoad import load_session
from utils.validateInput import validate_inputs

def get_driver_lap_data(year: int, gran_prix: str, session_type: str, driver: str, lap_number: int):

  validate_inputs(year, gran_prix , session_type )
  try:
    race_session = load_session(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

  driver_lap_data = race_session.laps.pick_drivers(driver).pick_laps(lap_number)
  if driver_lap_data.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  car_data = driver_lap_data.get_car_data()

  return {
    "track": race_session.event['EventName'],
    "compound":driver_lap_data["Compound"].iloc[0],
    "lap_data": driver_lap_data.to_dict(orient="list"),
    "car_data": car_data.to_dict(orient="list")
  }

def get_driver_laps(year: int, gran_prix: str, session_type: str, driver: str):
  
  validate_inputs(year, gran_prix , session_type )
  try:
    race_session = load_session(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  
  driver_lap_info = race_session.laps.pick_drivers(driver)
  if driver_lap_info.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  # Replace NaN, Infinity, and -Infinity with None in the DataFrame
  driver_lap_info = driver_lap_info.replace([float('inf'), float('-inf')], None).fillna(value="None")

  formattedDriverLapInfo = driver_lap_info.to_dict(orient="list")
  return {
    "laps": formattedDriverLapInfo
  }