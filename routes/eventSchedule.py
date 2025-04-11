import fastf1
from fastapi import HTTPException

def get_event_schedule(year: int):
  
  event_schedule = fastf1.get_event_schedule(year)
  
  if event_schedule.empty:
    raise HTTPException(status_code=404, detail="The schedule for this year does not exist or isnt available yet!")
  return {
    "schedule": event_schedule.to_dict(orient="list") 
  }