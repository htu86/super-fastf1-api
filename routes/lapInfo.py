from fastapi import HTTPException
import fastf1

def getDriverLapData(year: int, gp: str, session_type: str, driver: str, lap_number: int):
  # Endpoint to retrieve car data and lap data for a specific driver and lap number.

  # fastf1.Cache.enable_cache("./cache")  # Enable caching for better performance
  raceSession = fastf1.get_session(year, gp, session_type)
  raceSession.load(telemetry=True)

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