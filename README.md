# Super-FastF1 API

An api built on top of the [FastF1](https://github.com/theOehrly/Fast-F1) library.

 Documentation can be found: [Here](DOCS.md)

 
### Quickstart to run locally:
* `git clone https://github.com/htu86/super-f1-telemetry-api.git`
* `cd super-fastf1-api`

Creating a virtual enviroment:
* `python3  -m  venv  venv`

Activating virtual enviroment:
* ```sh source myenv/bin/activate # For mac/linux``` 
* ```myenv\Scripts\activate # For windows```

Installing dependencies:
* `pip install -r fastf1 uvicorn "fastapi[standard]"`

To host the api on your own machine, run:
* `uvicorn main:app --reload`

