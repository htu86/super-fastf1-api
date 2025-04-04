from utils.sessionLoad import loadSession
from fastapi import HTTPException
from utils.validateInput import validateInputs

def getCircuitInformation(year: int, granPrix: str, sessionType: str):
  validateInputs(year, granPrix , sessionType )  

  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")

  circuitInformation = raceSession.get_circuit_info()
  circuitCorners = circuitInformation.corners.to_dict("list") 
  circuitRotation = circuitInformation.rotation 
  marshallSectors = circuitInformation.marshal_sectors.to_dict("list")  
  marshallLights = circuitInformation.marshal_lights.to_dict("list")  

  if not circuitCorners or not circuitRotation or not marshallLights or not marshallSectors:
    raise HTTPException(status_code=404, detail="Circuit data not found or no data available.")

  return {
    "corners": circuitCorners,
    "rotation": circuitRotation,
    "marshall_sectors": marshallSectors,
    "marshall_lights": marshallLights
  }


def getTrackStatusHistory(year: int, granPrix: str, sessionType: str):
  validateInputs(year, granPrix , sessionType )    

  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")

  trackStatusHistory = raceSession.track_status.to_dict(orient="list")

  if not trackStatusHistory:
    raise HTTPException(status_code=404, detail="Track status history data not found or no data available.")  

  return {
    "track_status_history": trackStatusHistory
  }