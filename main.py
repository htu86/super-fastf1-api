from fastapi import FastAPI
from routes.carTelemetry import (
    getDriverLapData,
    getFastestSessionLap,
    getDriverPersonalBestLap,
    getDriverLaps
)

app = FastAPI()

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