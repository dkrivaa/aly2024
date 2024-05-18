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
# Working with the results
total_number_of_expenses = response_json['total']
expenses = response_json['items']
data_list = []
keys_list = ['id', 'paymentType', 'currency', 'currencyRate', 'amountExcludeVat', 'vat',
             'amountLocal', 'amountExcludeLocal', 'paymentAmountLocal', 'amount', 'date',
             'reportingDate', 'creationDate', 'lastUpdateDate',
             'accountingClassification.title', 'accountingClassification.income',
             'accountingClassification.vat', 'accountingClassification.mixed',
             'supplier.name', 'deductibleAmount', 'deductibleVat','businessAmount',
             'description']
data_list.append(keys_list)
for expense in expenses:
    # Extract values corresponding to the keys to keep
    values_list = [expense[key] for key in keys_list if key in expense]
    data_list.append(values_list)
# book.worksheet('test').update([keys_list, values_list], major_dimension='COLUMNS')
print(data_list[0])
print(data_list[1])
print(expenses[0])



