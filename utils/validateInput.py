from fastapi import HTTPException

def validate_inputs(year: int, gran_prix: str, session_type: str):
  if year < 1950 or year > 2025:
    raise HTTPException(status_code=400, detail="Invalid year provided.")
  if not gran_prix or not isinstance(gran_prix, str):
    raise HTTPException(status_code=400, detail="Invalid Grand Prix name provided.")
  if session_type not in ["P", "Q", "R"]:
    raise HTTPException(status_code=400, detail="Invalid session type provided.")