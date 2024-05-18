import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import json

from general.general_functions import openGoogle
from general.morning_key import getJWT

# Getting all expenses from a certain date

# opening Google workbook
book = openGoogle()
# Getting JWT token for morning
JWT = getJWT()
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
total_number_of_expenses = response_json['total']
expenses = response_json['items']
data_list = []
keys_list = list(expenses[0].keys())
data_list.append(keys_list)
for expense in expenses:
    values_list = list(expense.values())
    data_list.append(values_list)
# book.worksheet('test').update([keys_list, values_list], major_dimension='COLUMNS')
print(total_number_of_expenses)
print(expenses[0])



