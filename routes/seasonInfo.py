from fastapi import HTTPException
import fastf1

def getSessioninfo(year: int, granPrix: str, sessionType: str):
  raceSession = fastf1.get_session(year, granPrix, sessionType)
  raceSession.load()
  
  sessionInfo = raceSession.session_info
  if not sessionInfo:
    raise HTTPException(status_code=404, detail="Session data not found or no session data available.")

  sessionStatus = raceSession.session_status

  return {
    "session_info": sessionInfo,
    "session_timestamp": sessionStatus
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