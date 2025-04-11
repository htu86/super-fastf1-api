from fastapi import HTTPException
from utils.sessionLoad import loadSession
from utils.validateInput import validateInputs

def get_session_info(year: int, gran_prix: str, session_type: str):
  validateInputs(year, gran_prix , session_type )
  try:
    race_session = loadSession(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  
  session_info = race_session.session_info
  if not session_info:
    raise HTTPException(status_code=404, detail="Session data not found or no data available.")

  return {
    "session_info": session_info,
  }

def get_session_timing_data(year: int, gran_prix: str, session_type: str):
  validateInputs(year, gran_prix , session_type )
  try:
    race_session = loadSession(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  
  
  session_timing_data = race_session.session_status
  if session_timing_data is None:
    raise HTTPException(status_code=404, detail="Session data not found or no data available.")
  
  return {
    "session_timestamp": session_timing_data
  }

def get_session_weather_data(year: int, gran_prix: str, session_type: str):
  race_session = loadSession(year, gran_prix, session_type)
  
  weather_data = race_session.weather_data
  if weather_data is None or len(weather_data) == 0:
    raise HTTPException(status_code=404, detail="Weather data not found or no data available.")
  
  return {
    "weather": weather_data.to_dict(orient="list")
  }

def get_drivers_in_session(year: int, gran_prix: str, session_type: str):
  validateInputs(year, gran_prix , session_type )
  try:
    race_session = loadSession(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

  session_drivers = race_session.drivers
  if not session_drivers:
    raise HTTPException(status_code=404, detail="Driver data not found or no data available.")

  all_driver_info = []
  for driver in session_drivers:
    driver_info = race_session.get_driver(driver)
    all_driver_info.append(driver_info)

  return {
    "drivers": all_driver_info
  }

def get_session_race_control_messages(year: int, gran_prix: str, session_type: str):
  validateInputs(year, gran_prix , session_type )
  try:
    race_session = loadSession(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

  race_control_messages = race_session.race_control_messages
  race_control_messages = race_control_messages.replace([float('inf'), float('-inf')], None).fillna(value="None")
  
  if race_control_messages is None or len(race_control_messages) == 0:
    raise HTTPException(status_code=404, detail="Race control data not found or no data available.")
  
  return {
    "race_control_messages": race_control_messages.to_dict(orient="list") 
  }

