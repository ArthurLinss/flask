"""
test script to test api for dataframe handling
"""

import requests
import pandas as pd

# pseudo data
data = {'name': ['alpha', 'beta', 'gamma'],
        'value': [10, 20, 30]}

df = pd.DataFrame(data)

baseUrl = 'http://127.0.0.1:5000'
url = baseUrl + '/api/df'

json_data = df.to_dict(orient='records')
response = requests.post(url, json=json_data)
print("response: ", response, response.status_code)
if response.status_code == 200:
    updated_df = pd.read_json(response.json()['updated_dataframe'])
    print("Updated DataFrame:")
    print(updated_df.head())
else:
    print(f"Error: {response.status_code} - {response.json()['error']}")
