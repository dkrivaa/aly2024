import os
import requests
import json


# Function to get JWT (Json Web Token) to make requests
def getJWT():
    morning_key = os.environ.get('morning_key')
    url = 'https://api.greeninvoice.co.il/api/v1/account/token'
    data = {
        "id": "a0ed6cd1-e3e2-42ef-8f68-e9875255ec31",
        "secret": f'{morning_key}'
    }
    response = requests.post(url, json=data)

    response_json = json.loads(response.text)
    JWT = response_json['token']
    return JWT




