import fastf1
from utils.sessionLoad import loadSession

def getCircuitInformation(year: int, granPrix: str, sessionType: str):
  raceSession = loadSession(year, granPrix, sessionType)

  circuitInformation = raceSession.get_circuit_info()
  return {
    "corners":circuitInformation.corners.to_dict(orient="list"),
    "rotation": circuitInformation.rotation,
    "marshall_sectors": circuitInformation.marshal_sectors.to_dict(orient="list"),
    "marshall_lights": circuitInformation.marshal_lights.to_dict(orient="list")
  }

def getTrackStatusHistory(year: int, granPrix: str, sessionType: str):
  raceSession = loadSession(year, granPrix, sessionType)

  trackStatusHistory = raceSession.track_status.to_dict(orient="list")
  return {
    "track_status_history": trackStatusHistory
  }
