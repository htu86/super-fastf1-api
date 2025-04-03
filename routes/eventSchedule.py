import fastf1
from fastapi import HTTPException

def getEventSchedule(year: int):
  
  eventSchedule = fastf1.get_event_schedule(year)
  
  if eventSchedule.empty:
    raise HTTPException(status_code=404, detail="The schedule for this year does not exist or isnt available yet!")
  return {
    "schedule": eventSchedule.to_dict(orient="list") 
  }