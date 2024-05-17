import requests
import json
import os
import general_functions
import morning

# Getting all expenses from a certain date

# opening Google workbook
book = general_functions.openGoogle()
# Getting JWT token for morning
JWT = morning.getJWT()
date = os.environ.get('date')
# Getting all expenses from given date
url = 'https://api.greeninvoice.co.il/api/v1/expenses/search'
data = {
    "fromDate": "2016-01-01",
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {JWT}'
}

response = requests.post(url, json=data, headers=headers)

response_json = json.loads(response.text)
expense = response_json['items'][0]
print(response.text)
print(expense)


