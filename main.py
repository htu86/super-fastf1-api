from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
from fastapi.responses import JSONResponse

fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

app = FastAPI()

@app.get("/lap-data-info-driver/{year}/{gp}/{session_type}/{driver}/{lap_number}")
def getDriverLapData(year: int, gp: str, session_type: str, driver: str, lap_number: int):
    # Endpoint to retrieve car data and lap data for a specific driver and lap number.

    # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
    session = fastf1.get_session(year, gp, session_type)
    session.load(telemetry=True)

    driver_data = session.laps.pick_drivers(driver).pick_laps(lap_number)
    if driver_data.empty:
        raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

    car_data = driver_data.get_car_data()
    lap_data = driver_data.to_dict(orient="list")  # Convert lap data to a JSON-serializable dictionary
    car_data_dict = car_data.to_dict(orient="list")  # Convert car data to a JSON-serializable dictionary


    return {
        "lap_data": lap_data,
        "car_data": car_data_dict
    }

@app.get("/fastest-session-lap-info/{year}/{gp}/{session_type}")
def getFastestLapInfo(year: int, gp: str, session_type: str):
    # Endpoint to retrieve the fastest lap info in a session.

    # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
    session = fastf1.get_session(year, gp, session_type)
    session.load()

    fastest_lap = session.laps.pick_fastest()
    fastest_lap_car_data = fastest_lap.get_car_data().to_dict(orient="list")
    if fastest_lap.empty:
        raise HTTPException(status_code=404, detail="No lap data available for the session.")

    return {
        "driver": fastest_lap['Driver'],
        "lap_time": str(fastest_lap['LapTime']),
        "lap_number": int(fastest_lap['LapNumber']),
        "team": fastest_lap['Team'],
        "car_data": fastest_lap_car_data
}

@app.get("/personal-best-lap/{year}/{gp}/{session_type}/{driver}")
def getDriverPersonalBestLap(year: int, gp: str | int, session_type: str, driver: str):
    # Endpoint to retrieve the personal best lap info for a specific driver in a session.

    # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
    session = fastf1.get_session(year, gp, session_type)
    session.load()

    driver_data = session.laps.pick_drivers(driver)
    if driver_data.empty:
        raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

    personal_best_lap = driver_data.pick_fastest()
    if personal_best_lap.empty:
        raise HTTPException(status_code=404, detail="No lap data available for the driver.")

    personal_best_lap_car_data = personal_best_lap.get_car_data().to_dict(orient="list")
    if personal_best_lap.empty:
        raise HTTPException(status_code=404, detail="No lap data available for the session.")
    return {
        "driver": personal_best_lap['Driver'],
        "lap_time": str(personal_best_lap['LapTime']),
        "lap_number": int(personal_best_lap['LapNumber']),
        "team": personal_best_lap['Team'],
        "car_data": personal_best_lap_car_data
}
