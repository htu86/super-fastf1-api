from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
from fastapi.responses import JSONResponse

fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

app = FastAPI()

@app.get("/driver-lap-telemetry/{year}/{gp}/{session_type}/{driver}/{lap_number}")
def getDriverLapData(year: int, gp: str, session_type: str, driver: str, lap_number: int):
  # Endpoint to retrieve car data and lap data for a specific driver and lap number.

  # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
  raceSession = fastf1.get_session(year, gp, session_type)
  raceSession.load(telemetry=True)

  driverData = raceSession.laps.pick_drivers(driver).pick_laps(lap_number)
  if driverData.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  car_data = driverData.get_car_data()
  lap_data = driverData.to_dict(orient="list")  # Convert lap data to a JSON-serializable dictionary
  car_data_dict = car_data.to_dict(orient="list")  # Convert car data to a JSON-serializable dictionary


  return {
    "track": raceSession.event['EventName'],
    "compound":driverData["Compound"].iloc[0],
    "lap_data": lap_data,
    "car_data": car_data_dict
  }

@app.get("/fastest-session-lap-telemetry/{year}/{gp}/{session_type}")
def getFastestLapInfo(year: int, gp: str, session_type: str):
  # Endpoint to retrieve the fastest lap info in a session.

  # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
  try:
    raceSession = fastf1.get_session(year, gp, session_type)
    raceSession.load()
  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Error loading session: {str(e)}")

  if raceSession.event['EventName'] is None:
    raise HTTPException(status_code=404, detail="Grand Prix not found.")

  fastestSessionLap = raceSession.laps.pick_fastest()
  if fastestSessionLap.empty:
    raise HTTPException(status_code=404, detail="No lap data available for the session.")

  carData = fastestSessionLap.get_car_data().to_dict(orient="list")

  return {
    "track": raceSession.event['EventName'],
    "driver": fastestSessionLap['Driver'],
    "lap_time": str(fastestSessionLap['LapTime']),
    "lap_number": int(fastestSessionLap['LapNumber']),
    "team": fastestSessionLap['Team'],
    "compound": fastestSessionLap.laps["Compound"].iloc[0],
    "car_data": carData
  }

@app.get("/personal-best-lap-telemetry/{year}/{gp}/{session_type}/{driver}")
def getDriverPersonalBestLap(year: int, gp: str | int, session_type: str, driver: str):
    # Endpoint to retrieve the personal best lap info for a specific driver in a session.

    # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
  raceSession = fastf1.get_session(year, gp, session_type)
  raceSession.load()

  driverData = raceSession.laps.pick_drivers(driver)
  if driverData.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  driverBestLap = driverData.pick_fastest()
  if driverBestLap.empty:
    raise HTTPException(status_code=404, detail="No lap data available for the driver.")

  personal_best_lap_car_data = driverBestLap.get_car_data().to_dict(orient="list")
  if driverBestLap.empty:
    raise HTTPException(status_code=404, detail="No lap data available for the session.")
  
  return {
    "driver": driverBestLap['Driver'],
    "lap_time": str(driverBestLap['LapTime']),
    "lap_number": int(driverBestLap['LapNumber']),
    "team": driverBestLap['Team'],
    "car_data": personal_best_lap_car_data
}

@app.get("/driver-laps/{year}/{gp}/{session_type}/{driver}")
def getDriverLaps(year: int, gp: str, session_type: str, driver: str):
  
  raceSession = fastf1.get_session(year, gp, session_type)
  raceSession.load()
  
  driverLapInfo = raceSession.laps.pick_drivers(driver)
  if driverLapInfo.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  # Replace NaN, Infinity, and -Infinity with None in the DataFrame
  driverLapInfo = driverLapInfo.replace([float('inf'), float('-inf')], None).fillna(value="None")

  # Convert lap data to a JSON-serializable dictionary
  formattedDriverLapInfo = driverLapInfo.to_dict(orient="list")
  return {
    "laps": formattedDriverLapInfo
  }