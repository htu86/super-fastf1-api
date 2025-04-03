import fastf1

def loadSession(sessionYear: int, grandPrix: str, sessionType: str):
  raceSession = fastf1.get_session(sessionYear, grandPrix, sessionType)
  raceSession.load()
  
  return raceSession