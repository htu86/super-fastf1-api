from fastapi import FastAPI

from routes.lapInfo import (
  get_driver_lap_data,
  get_driver_laps
)
from routes.sessionInfo import (
  get_drivers_in_session,
  get_session_info,
  get_session_race_control_messages,
  get_session_timing_data,
  get_session_weather_data
)
from routes.lapRecords import(
  get_driver_personal_best_lap,
  get_fastest_session_lap
)
from routes.trackInfo import(
  get_track_status_history,
  get_circuit_info
)
from routes.eventSchedule import (
  get_event_schedule
)

app = FastAPI()

# Endpoints related to lap data

@app.get("/driver-lap-telemetry/{year}/{gp}/{session_type}/{driver}/{lap_number}")
def driver_lap_telemetry(year: int, gp: str, session_type: str, driver: str, lap_number: int):
  return get_driver_lap_data(year, gp, session_type, driver, lap_number)

@app.get("/fastest-session-lap-telemetry/{year}/{gp}/{session_type}")
def fastest_session_lap_telemetry(year: int, gp: str, session_type: str):
  return get_fastest_session_lap(year, gp, session_type)

@app.get("/personal-best-lap-telemetry/{year}/{gp}/{session_type}/{driver}")
def personal_best_lap_telemetry(year: int, gp: str, session_type: str, driver: str):
  return get_driver_personal_best_lap(year, gp, session_type, driver)

@app.get("/driver-laps/{year}/{gp}/{session_type}/{driver}")
def driver_laps(year: int, gp: str, session_type: str, driver: str):
  return get_driver_laps(year, gp, session_type, driver)

# Endpoints related to session information

@app.get("/session-info/{year}/{gp}/{session_type}")
def session_info(year: int, gp: str, session_type: str):
  return get_session_info(year, gp, session_type)

@app.get("/session-weather/{year}/{gp}/{session_type}")
def session_weather(year: int, gp: str, session_type: str):
  return get_session_weather_data(year, gp, session_type)

@app.get("/session-drivers/{year}/{gp}/{session_type}")
def session_drivers(year: int, gp: str, session_type: str):
  return get_drivers_in_session(year, gp, session_type)  

@app.get("/session-time/{year}/{gp}/{session_type}")
def session_time(year: int, gp: str, session_type: str):
  return get_session_timing_data(year, gp, session_type) 

@app.get("/session-race-control-messages/{year}/{gp}/{session_type}")
def race_control_messages(year: int, gp: str, session_type: str):
  return get_session_race_control_messages(year, gp, session_type)

# Event schedule


@app.get("/event-schedule/{year}")
def event_schedule(year: int):
  return get_event_schedule(year)

# Endpoints related to track information

@app.get("/circuit-geographic-data/{year}/{gp}/{session_type}")
def circuit_info(year: int, gp: str, session_type: str):
  return get_circuit_info(year, gp, session_type)

@app.get("/track-status-history/{year}/{gp}/{session_type}")
def track_status_history(year: int, gp: str, session_type: str):
  return get_track_status_history(year, gp, session_type)
