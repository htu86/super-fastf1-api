import time
from functools import wraps
from fastapi import (
  HTTPException  
)

# Function to limit the amount of api requests 
# TODO: Store calls in database so if server crashes or resets, the amount of calls stays the same

def rate_limit(max_calls: int, max_time: int):
  def decorator(func):
    calls = []
    @wraps(func)
    async def wrapper(*args, **kwargs):
      now = time.time()
      calls_in_time_frame = [call for call in calls if call > now - max_time]
      if(len(calls_in_time_frame) >= max_calls):
        raise HTTPException(status_code=400, detail=f"You have exceeded the amount of requests in {max_time} seconds")
      calls.append(now)
      return func(*args, **kwargs)
    return wrapper
  return decorator