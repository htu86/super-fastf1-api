from fastapi import HTTPException
from utils.sessionLoad import load_session
from utils.validateInput import validate_inputs

def get_fastest_session_lap(year: int, gran_prix: str, session_type: str):
    # Endpoint to retrieve the fastest lap info in a session.

    validate_inputs(year, gran_prix, session_type)
    try:
      race_session = load_session(year, gran_prix, session_type)
    except Exception as e:
      raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")

    if race_session.event['EventName'] is None:
      raise HTTPException(status_code=404, detail="Grand Prix not found.")

    fastest_session_lap = race_session.laps.pick_fastest()
    if fastest_session_lap.empty:
      raise HTTPException(status_code=404, detail="No lap data available for the session.")

    car_data = fastest_session_lap.get_car_data().to_dict(orient="list")

    event_name = race_session.event['EventName']

    return {
      "track": event_name,  # Use event_name instead of fastest_session_lap.event
      "driver": fastest_session_lap['Driver'],
      "lap_time": str(fastest_session_lap['LapTime']),
      "lap_number": int(fastest_session_lap['LapNumber']),
      "team": fastest_session_lap['Team'],
      "compound": fastest_session_lap['Compound'],  # Fixed access to compound
      "car_data": car_data
    }

def get_driver_personal_best_lap(year: int, gran_prix: str, session_type: str, driver: str):

  validate_inputs(year, gran_prix , session_type )
  try:
    race_session = load_session(year, gran_prix, session_type)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load session: {str(e)}")
  

  driver_data = race_session.laps.pick_drivers(driver)
  if driver_data.empty:
    raise HTTPException(status_code=404, detail="Driver not found or no lap data available.")

  driver_best_lap = driver_data.pick_fastest()
  if driver_best_lap.empty:
    raise HTTPException(status_code=404, detail="No lap data available for the driver.")

  car_data = driver_best_lap.get_car_data()
  if driver_best_lap.empty:
    raise HTTPException(status_code=404, detail="No lap data available for the session.")
  
  return {
    "driver": driver_best_lap['Driver'],
    "lap_time": str(driver_best_lap['LapTime']),
    "lap_number": int(driver_best_lap['LapNumber']),
    "team": driver_best_lap['Team'],
    "car_data": car_data.to_dict(orient="list")
}