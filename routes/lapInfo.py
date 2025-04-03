from fastapi import HTTPException
import fastf1
from utils.sessionLoad import loadSession

def getDriverLapData(year: int, granPrix: str, sessionType: str, driver: str, lap_number: int):
  # Endpoint to retrieve car data and lap data for a specific driver and lap number.

  # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
  raceSession = loadSession(year, granPrix, sessionType)

  driverLapData = raceSession.laps.pick_drivers(driver).pick_laps(lap_number)
  if driverLapData.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  carData = driverLapData.get_car_data()

  return {
    "track": raceSession.event['EventName'],
    "compound":driverLapData["Compound"].iloc[0],
    "lap_data": driverLapData.to_dict(orient="list"),
    "car_data": carData.to_dict(orient="list")
  }

def getDriverLaps(year: int, granPrix: str, sessionType: str, driver: str):
  
  raceSession = loadSession(year, granPrix, sessionType)
  
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