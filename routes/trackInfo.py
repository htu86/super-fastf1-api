import fastf1

def getCircuitInformation(year: int, granPrix: str, sessionType: str):
  raceSession = fastf1.get_session(year, granPrix, sessionType)
  raceSession.load()  

  circuitInformation = raceSession.get_circuit_info()
  return {
    "corners":circuitInformation.corners.to_dict(orient="list"),
    "rotation": circuitInformation.rotation,
    "marshall_sectors": circuitInformation.marshal_sectors.to_dict(orient="list"),
    "marshall_lights": circuitInformation.marshal_lights.to_dict(orient="list")
  }

def getTrackStatusHistory(year: int, granPrix: str, sessionType: str):
  raceSession = fastf1.get_session(year, granPrix, sessionType)
  raceSession.load()  

  trackStatusHistory = raceSession.track_status.to_dict(orient="list")
  return {
    "track_status_history": trackStatusHistory
  }
