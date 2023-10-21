import datetime
import json
import csv

import requests


date=datetime.date.today()
date-=datetime.timedelta(days=1)
with open('data.csv', 'w', newline='',encoding="utf-8") as file:
    while date.year>2014:
        url = "https://www.cbr-xml-daily.ru/archive/" + f"{date.year}" + "/" + f"{date.month}" +"/"+ f"{date.day}" + "/daily_json.js"
        print(url)
        print(date.weekday())
        response = requests.get(url)
        data = json.loads(response.text)
        if date.weekday()==0 or date.weekday()==6 or date.weekday()==5:
            date-=datetime.timedelta(days=1)
            continue
        valute_data = data['Valute']
        wr=csv.writer(file)
        for valute in valute_data.values():    
            if valute['CharCode'] == 'USD':
                wr.writerow((f"Дата: {data['Date']}").split(','))
                wr.writerow((f"{valute['Name']} курс: {valute['Value']}").split(','))
        date-=datetime.timedelta(days=1)
    