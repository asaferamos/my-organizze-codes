#!/usr/bin/python

import sys
from helper import *
import requests
import json
from datetime import date

try:
  accont_from = str(sys.argv[1])
  account_to  = str(sys.argv[2])
  start_year  = int(sys.argv[3])
  start_month = int(sys.argv[4])
except:
    print('Missing arguments year and description')
    exit()

url_request = url + '/transactions'

today = date.today()
start_day = date(start_year, start_month, 1)

months = ( (today - start_day).days / 30 ) + 1

actual_year = start_year
actual_month = start_month

for month in range(1, months):
  if actual_month == 13:
    actual_month = 1
    actual_year = actual_year + 1

  month_string = str(actual_month)
  if actual_month < 10:
    month_string = '0' + str(actual_month)

  print(str(month_string) + '/' + str(actual_year))

  actual_month = actual_month + 1

  query = {
    'start_date': str(actual_year) + '-' + str(month_string) + '-01'
  }

  response = requests.request(
    'GET',
    url_request,
    headers=headers,
    params=query
  )

  data = json.loads(response.text)

  for transaction in data:
    if transaction['account_id'] == int(accont_from):
      response_put = requests.request(
        'PUT',
        url_request + '/' + str(transaction['id']),
        data={ "account_id" : int(account_to) },
        headers=headers
      )

      if (response_put.status_code == 201):
        print(
          'PUT ' + transaction['description'] + ' IN ' + transaction['date']
        )
