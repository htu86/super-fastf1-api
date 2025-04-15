import fastf1

def load_session(session_year: int, grand_prix: str, session_type: str):
  race_session = fastf1.get_session(session_year, grand_prix, session_type)
  race_session.load()
  
  return race_session