import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import json
import pandas as pd

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

# Working with the results from morning
total_number_of_expenses = response_json['total']
expenses = response_json['items']
# If there are any expenses in morning
if len(expenses) > 0:
    # list to hold all morning expenses
    data_list = []
    # list of keys of interest from morning data
    keys_list = ['id', 'paymentType', 'currency', 'currencyRate', 'amountExcludeVat', 'vat',
                 'amountLocal', 'amountExcludeLocal', 'paymentAmountLocal', 'amount', 'date',
                 'reportingDate', 'creationDate', 'lastUpdateDate',
                 'accountingClassification.title', 'accountingClassification.income',
                 'accountingClassification.vat', 'accountingClassification.mixed',
                 'supplier.name', 'deductibleAmount', 'deductibleVat','businessAmount',
                 'description']
    # Getting the Morning data and making list
    for expense in expenses:
        values_list = []
        for key in keys_list:
            keys = key.split('.')  # Split nested keys
            value = expense
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    value = None  # Handle missing keys
                    break
            values_list.append(value)
        data_list.append(values_list)
    # Getting existing expenses from Google sheet and making the id into list
    existing_expenses = pd.DataFrame(book.worksheet('expenses').get_all_records())
    if len(existing_expenses) > 0:
        existing_list = existing_expenses['id'].to_list()
        # keeping morning expenses not included in existing google sheet expenses and appending
        data_list = [x for x in data_list if x[0] not in existing_list]
    book.worksheet('expenses').append_rows(data_list)

# If no expenses in morning, do noting
else:
    pass








