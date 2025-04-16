# super fastf1 api documentation

> ### Table of contents
> * [Basic information](#basic-information)
> * [Driver Lap Telemetry](#driver-lap-telemetry)
> * [Driver All Laps Telemetry](#driver-all-laps-telemetry)
> * [Driver Fastest Lap Telemetry](#driver-fastest-lap-telemetry)
> * [Session Fastest Lap Telemetry](#session-fastest-lap-telemetry)
> * [Session Info](#session-info)
> * [Session Weather](#session-weather)
> * [Session Drivers](#session-drivers)
> * [Session Time](#session-time)
> * [Session RC Messages](#session-rc-messages)
> * [Circuit Geographic Data](#circuit-geographic-data)
> * [Circuit Status History](#circuit-status-history)
> * [Event Schedule](#event-schedule)

---
## Basic information

* All of the requests use the `GET` method
* All requests returns JSON files

---
## Driver Lap Telemetry

 ` /driver-lap-telemetry/{year}/{gp}/{session_type}/{driver}/{lap_number}`

**Description:** Retrieves basic information about the driver and track along with car telemetry data for a specific driver's lap.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type (e.g., "qualifying", "race").
- `driver` (str): The driver's identifier.
- `lap_number` (int): The lap number to retrieve telemetry for.


---
## Driver All Laps Telemetry

`/driver-all-laps-telemetry/{year}/{gp}/{session_type}/{driver}`

**Description:** Retrieves basic information along with car telemetry data for all laps of a specific driver.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.
- `driver` (str): The driver's identifier.

---
## Driver Fastest Lap Telemetry
`/driver-fastest-lap-telemetry/{year}/{gp}/{session_type}/{driver}`

**Description:** Retrieves basic information about the driver and track along with car telemetry data for the fastest lap of a specific driver.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.
- `driver` (str): The driver's identifier.

---
## Session Fastest Lap Telemetry

`/session-fastest-lap-telemetry/{year}/{gp}/{session_type}`

**Description:** Retrieves telemetry data for the overall fastest lap in the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---
## Session Info

`/session-info/{year}/{gp}/{session_type}`

**Description:** Retrieves general information about the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---
## Session Weather

`/session-weather/{year}/{gp}/{session_type}`

**Description:** Retrieves weather data for the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## Session Drivers

`/session-drivers/{year}/{gp}/{session_type}`

**Description:** Retrieves a list of drivers participating in the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## Session Time

`/session-time/{year}/{gp}/{session_type}`

**Description:** Retrieves the session's start and end times.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## Session RC Messages

`/session-rc-messages/{year}/{gp}/{session_type}`

**Description:** Retrieves race control messages for the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## Circuit Geographic Data

`/circuit-geographic-data/{year}/{gp}/{session_type}`

**Description:** Retrieves geographic data for the circuit.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## Circuit Status History

`/circuit-status-history/{year}/{gp}/{session_type}`


**Description:** Retrieves the status history of the circuit during the session.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.
- `gp` (str): The Grand Prix name.
- `session_type` (str): The session type.

---

## Event Schedule

`/event-schedule/{year}`

**Description:** Retrieves the schedule of events for the race year.  
**Method:** `GET`  
**Parameters:**
- `year` (int): The year of the event.