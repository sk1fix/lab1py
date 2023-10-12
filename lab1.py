import datetime
import json
import csv

import requests


date=datetime.date.today()

print(date)
while date.year>2014:
    url = "https://www.cbr-xml-daily.ru/archive/" + date.year + "/" +date.month +"/"+ date.day + "/daily_json.js"
    response = requests.get(url)
    data = json.loads(response.text)
    if date.weekday==0 or date.weekday==6:
        
        continue
    





with open('data.csv', 'w', newline='',encoding="utf-8") as file:
    valute_data = data['Valute']
    wr=csv.writer(file)
    for valute in valute_data.values():    
        if valute['CharCode'] == 'USD':
            wr.writerow((f"Дата: {data['Date']}").split(','))
            wr.writerow((f"{valute['Name']} курс: {valute['Value']}").split(','))