# super fastf1 api documentation

> ### Table of contents
> * [Basic information](#basic-information)
> * [/driver-lap-telemetry](#driver-lap-telemetry)
> * [/driver-all-laps-telemetry](#driver-all-laps-telemetry)
> * [/driver-fastest-lap-telemetry](#driver-fastest-lap-telemetry)
> * [/session-fastest-lap-telemetry](#session-fastest-lap-telemetry)
> * [/session-info](#session-info)
> * [/session-weather](#session-weather)
> * [/session-drivers](#session-drivers)
> * [/session-time](#session-time)
> * [/session-rc-messages](#session-rc-messages)
> * [/circuit-geographic-data](#circuit-geographic-data)
> * [/circuit-status-history](#circuit-status-history)
> * [/event-schedule](#event-schedule)

---
## Basic information

* All of the requests use the `GET` method
* All requests returns JSON files

---

## /driver-lap-telemetry/{year}/{gp}/{session_type}/{driver}/{lap_number}
**Description:** Retrieves basic information about the driver and track along with car telemetry data for a specific driver's lap.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type (e.g., "qualifying", "race").
- `driver` (str): The driver's identifier.
- `lap_number` (int): The lap number to retrieve telemetry for.


---

## /driver-all-laps-telemetry/{year}/{gp}/{session_type}/{driver}
**Description:** Retrieves basic information along with car telemetry data for all laps of a specific driver.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.
- `driver` (str): The driver's identifier.

---

## /driver-fastest-lap-telemetry/{year}/{gp}/{session_type}/{driver}
**Description:** Retrieves basic information about the driver and track along with car telemetry data for the fastest lap of a specific driver.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.
- `driver` (str): The driver's identifier.

---

## /session-fastest-lap-telemetry/{year}/{gp}/{session_type}
**Description:** Retrieves telemetry data for the overall fastest lap in the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /session-info/{year}/{gp}/{session_type}
**Description:** Retrieves general information about the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /session-weather/{year}/{gp}/{session_type}
**Description:** Retrieves weather data for the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /session-drivers/{year}/{gp}/{session_type}
**Description:** Retrieves a list of drivers participating in the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /session-time/{year}/{gp}/{session_type}
**Description:** Retrieves the session's start and end times.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /session-rc-messages/{year}/{gp}/{session_type}
**Description:** Retrieves race control messages for the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /circuit-geographic-data/{year}/{gp}/{session_type}
**Description:** Retrieves geographic data for the circuit.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /circuit-status-history/{year}/{gp}/{session_type}
**Description:** Retrieves the status history of the circuit during the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## /event-schedule/{year}
**Description:** Retrieves the schedule of events for the race weekend.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.