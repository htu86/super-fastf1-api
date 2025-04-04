from fastapi import HTTPException

def validateInputs(year: int, granPrix: str, sessionType: str):
  if year < 1950 or year > 2025:
    raise HTTPException(status_code=400, detail="Invalid year provided.")
  if not granPrix or not isinstance(granPrix, str):
    raise HTTPException(status_code=400, detail="Invalid Grand Prix name provided.")
  if sessionType not in ["P", "Q", "R"]:
    raise HTTPException(status_code=400, detail="Invalid session type provided.")