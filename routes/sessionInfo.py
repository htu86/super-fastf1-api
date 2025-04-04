from fastapi import HTTPException
from utils.sessionLoad import loadSession
from utils.validateInput import validateInputs

def getSessioninfo(year: int, granPrix: str, sessionType: str):
  validateInputs(year, granPrix , sessionType )
  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  
  sessionInfo = raceSession.session_info
  if not sessionInfo:
    raise HTTPException(status_code=404, detail="Session data not found or no data available.")

  return {
    "session_info": sessionInfo,
  }

def getSessionTimingData(year: int, granPrix: str, sessionType: str):
  validateInputs(year, granPrix , sessionType )
  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  
  
  sessionTimingData = raceSession.session_status
  if sessionTimingData is None:
    raise HTTPException(status_code=404, detail="Session data not found or no data available.")
  
  return {
    "session_timestamp": sessionTimingData
  }

def getSessionWeatherData(year: int, granPrix: str, sessionType: str):
  raceSession = loadSession(year, granPrix, sessionType)
  
  weatherData = raceSession.weather_data
  if weatherData is None or len(weatherData) == 0:
    raise HTTPException(status_code=404, detail="Weather data not found or no data available.")
  
  return {
    "weather": weatherData.to_dict(orient="list")
  }

def getDriversInSession(year: int, granPrix: str, sessionType: str):
  validateInputs(year, granPrix , sessionType )
  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

  sessionDrivers = raceSession.drivers
  if not sessionDrivers:
    raise HTTPException(status_code=404, detail="Driver data not found or no data available.")

  allDriverInfo = []
  for sessionDriver in sessionDrivers:
    driverInfo = raceSession.get_driver(sessionDriver)
    allDriverInfo.append(driverInfo)

  return {
    "drivers": allDriverInfo  
  }

def getSessionRaceControlMessages(year: int, granPrix: str, sessionType: str):
  validateInputs(year, granPrix , sessionType )
  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

  raceControlMessages = raceSession.race_control_messages
  raceControlMessages = raceControlMessages.replace([float('inf'), float('-inf')], None).fillna(value="None")
  
  if raceControlMessages is None or len(raceControlMessages) == 0:
    raise HTTPException(status_code=404, detail="Race control data not found or no data available.")
  
  return {
    "race_control_messages": raceControlMessages.to_dict(orient="list") 
  }

