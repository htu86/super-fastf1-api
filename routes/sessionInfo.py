from fastapi import HTTPException
import fastf1

def getSessioninfo(year: int, granPrix: str, sessionType: str):
  raceSession = fastf1.get_session(year, granPrix, sessionType)
  raceSession.load()
  
  sessionInfo = raceSession.session_info
  if not sessionInfo:
    raise HTTPException(status_code=404, detail="Session data not found or no session data available.")

  return {
    "session_info": sessionInfo,
  }

def getSessionTimingData(year: int, granPrix: str, sessionType: str):
  raceSession = fastf1.get_session(year, granPrix, sessionType)
  raceSession.load()
  
  sessionTimingData = raceSession.session_status
  
  return {
    "session_timestamp": sessionTimingData
  }

def getSessionWeatherData(year: int, granPrix: str, sessionType: str):
  raceSession = fastf1.get_session(year, granPrix, sessionType)
  raceSession.load()
  
  weatherData = raceSession.weather_data
  if weatherData is None or len(weatherData) == 0:
    raise HTTPException(status_code=404, detail="Weather data not found or no weather data available.")
  
  return {
    "weather": weatherData.to_dict(orient="list")
  }

def getDriversInSession(year: int, gp: str, sessionType: str):
  raceSession = fastf1.get_session(year, gp, sessionType)
  raceSession.load()  

  sessionDrivers = raceSession.drivers
  if not sessionDrivers:
    raise HTTPException(status_code=404, detail="Session data not found or no session data available.")

  allDriverInfo = []
  for sessionDriver in sessionDrivers:
    driverInfo = raceSession.get_driver(sessionDriver)
    allDriverInfo.append(driverInfo)

  return {
    "drivers": allDriverInfo  
  }

def getSessionRaceControlMessages(year: int, gp: str, sessionType: str):
  raceSession = fastf1.get_session(year, gp, sessionType)
  raceSession.load(messages=True)
  
  raceControlMessages = raceSession.race_control_messages
  raceControlMessages = raceControlMessages.replace([float('inf'), float('-inf')], None).fillna(value="None")
  
  if raceControlMessages is None or len(raceControlMessages) == 0:
    raise HTTPException(status_code=404, detail="Race control data not found or no race control data available.")
  
  return {
    "race_control_messages": raceControlMessages.to_dict(orient="list") 
  }
