import fastf1
from fastapi import HTTPException
from utils.sessionLoad import loadSession
from utils.validateInput import validateInputs

def getFastestSessionLap(year: int, granPrix: str, sessionType: str):
  # Endpoint to retrieve the fastest lap info in a session.

  validateInputs(year, granPrix , sessionType )
  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

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

def getDriverPersonalBestLap(year: int, granPrix: str, sessionType: str, driver: str):

  validateInputs(year, granPrix , sessionType )
  try:
    raceSession = loadSession(year, granPrix, sessionType)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

  driverData = raceSession.laps.pick_drivers(driver)
  if driverData.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  driverBestLap = driverData.pick_fastest()
  if driverBestLap.empty:
    raise HTTPException(status_code=404, detail="No lap data available for the driver.")

  bestLapCarData = driverBestLap.get_car_data()
  if driverBestLap.empty:
    raise HTTPException(status_code=404, detail="No lap data available for the session.")
  
  return {
    "driver": driverBestLap['Driver'],
    "lap_time": str(driverBestLap['LapTime']),
    "lap_number": int(driverBestLap['LapNumber']),
    "team": driverBestLap['Team'],
    "car_data": bestLapCarData.to_dict(orient="list")
}