from fastapi import FastAPI
from routes.lapInfo import (
  getDriverLapData,
  getDriverLaps
)
from routes.sessionInfo import (
  getSessioninfo,
  getSessionWeatherData , 
  getDriversInSession,
  getSessionTimingData,
  getSessionRaceControlMessages
)
from routes.lapRecords import(
  getDriverPersonalBestLap,
  getFastestSessionLap
)
from routes.trackInfo import(
  getCircuitInformation,
  getTrackStatusHistory  
)
from routes.eventSchedule import (
  getEventSchedule
)

app = FastAPI()

# Endpoints related to lap data

@app.get("/driver-lap-telemetry/{year}/{gp}/{session_type}/{driver}/{lap_number}")
def driver_lap_telemetry(year: int, gp: str, session_type: str, driver: str, lap_number: int):
  return getDriverLapData(year, gp, session_type, driver, lap_number)

@app.get("/fastest-session-lap-telemetry/{year}/{gp}/{session_type}")
def fastest_session_lap_telemetry(year: int, gp: str, session_type: str):
  return getFastestSessionLap(year, gp, session_type)

@app.get("/personal-best-lap-telemetry/{year}/{gp}/{session_type}/{driver}")
def personal_best_lap_telemetry(year: int, gp: str, session_type: str, driver: str):
  return getDriverPersonalBestLap(year, gp, session_type, driver)

@app.get("/driver-laps/{year}/{gp}/{session_type}/{driver}")
def driver_laps(year: int, gp: str, session_type: str, driver: str):
  return getDriverLaps(year, gp, session_type, driver)

# Endpoints related to session information

@app.get("/session-info/{year}/{gp}/{session_type}")
def session_info(year: int, gp: str, session_type: str):
  return getSessioninfo(year, gp, session_type)

@app.get("/session-weather/{year}/{gp}/{session_type}")
def session_weather(year: int, gp: str, session_type: str):
  return getSessionWeatherData(year, gp, session_type)

@app.get("/session-drivers/{year}/{gp}/{session_type}")
def session_drivers(year: int, gp: str, session_type: str):
  return getDriversInSession(year, gp, session_type)  

@app.get("/session-time/{year}/{gp}/{session_type}")
def session_time(year: int, gp: str, session_type: str):
  return getSessionTimingData(year, gp, session_type) 

@app.get("/session-race-control-messages/{year}/{gp}/{session_type}")
def race_control_messages(year: int, gp: str, session_type: str):
  return getSessionRaceControlMessages(year, gp, session_type)

# Event schedule

@app.get("/event-schedule/{year}")
def event_schedule(year: int):
  return getEventSchedule(year)


# Endpoints related to track information

@app.get("/circuit-geographic-data/{year}/{gp}/{session_type}")
def circuit_info(year: int, gp: str, session_type: str):
  return getCircuitInformation(year, gp, session_type)

@app.get("/track-status-history/{year}/{gp}/{session_type}")
def track_status_history(year: int, gp: str, session_type: str):
  return getTrackStatusHistory(year, gp, session_type)
