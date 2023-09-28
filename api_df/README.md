# About

This is a minimal example showing the interplay of three instances:
- backend with some code doing operations, in this case dataframe manipulations
- a flask api where the backend runs and can be accessed via post or get requests
- a test script to make requests to the api, e.g. posting a dataframe

# Usage

- run the server via `python api.py` in separate terminal
- make requests: `python test_api.py`
