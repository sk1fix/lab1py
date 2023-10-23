import datetime
import json
import csv

import requests


date=datetime.date.today()
date-=datetime.timedelta(days=1)
with open('data.csv', 'w', newline='',encoding="utf-8") as file:
    while date.year>2014:
        o1=""
        o2=""
        if date.month<10:
            o1=0
        if date.day<10:
            o2=0
        url = "https://www.cbr-xml-daily.ru/archive/" + f"{date.year}" + "/" +f"{o1}" + f"{date.month}" +"/"+f"{o2}" f"{date.day}" + "/daily_json.js"
        print(url)
        
        response = requests.get(url)
        data = json.loads(response.text)
        if 'Valute' not in data:
            date-=datetime.timedelta(days=1)
            continue
        if date.weekday()==0 or date.weekday()==6 :
            date-=datetime.timedelta(days=1)
            continue
        valute_data = data['Valute']
        wr=csv.writer(file)
        for valute in valute_data.values():    
            if valute['CharCode'] == 'USD':
                wr.writerow((f"Дата: {data['Date']}").split(','))
                wr.writerow((f"{valute['Name']} курс: {valute['Value']}").split(','))
        date-=datetime.timedelta(days=1)
    