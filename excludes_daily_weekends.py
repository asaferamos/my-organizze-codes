#!/usr/bin/python

import sys
from helper import *
import requests
import json
import datetime


try:
  year = str(sys.argv[1])
  description = str(sys.argv[2])
except:
    print('Missing arguments year and description')
    exit()

year = str(sys.argv[1])
description = str(sys.argv[2])

url_request = url + '/transactions'

for month in range(1,13):
  month_string = str(month)
  if month < 10:
    month_string = '0' + str(month)
  
  print('Month: ' + month_string)

  query = {
    'start_date': year + '-' + month_string + '-01'
  }

  response = requests.request(
    'GET',
    url_request,
    headers=headers,
    params=query
  )

  data = json.loads(response.text)

  for transaction in data:
    if transaction['description'] == description:
      if (transaction['recurring']) and not (transaction['paid']):
        dayweek = datetime.datetime.strptime(
          transaction['date'], '%Y-%m-%d'
        ).weekday()
        
        if (dayweek == 5) or (dayweek == 6):
          response_delete = requests.request(
            'DELETE',
            url_request + '/' + str(transaction['id']),
            headers=headers
          )

          if (response_delete.status_code == 200):
            print(
              'DELETE ' + transaction['description'] + ' IN ' + transaction['date']
            )
          