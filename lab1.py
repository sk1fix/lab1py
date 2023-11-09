import datetime
import json
import csv

import requests


my_date=datetime.date.today()
my_date-=datetime.timedelta(days=1)
with open('data.csv', 'w', newline='',encoding="utf-8") as file:
    while my_date.year>2014:
        o1=""
        o2=""
        if my_date.month<10:
            o1=0
        if my_date.day<10:
            o2=0
        url = "https://www.cbr-xml-daily.ru/archive/" + f"{my_date.year}" + "/" +f"{o1}" + f"{my_date.month}" +"/"+f"{o2}" f"{my_date.day}" + "/daily_json.js"
        print(url)
        
        response = requests.get(url)
        data = json.loads(response.text)
        if 'Valute' not in data:
            my_date-=datetime.timedelta(days=1)
            continue
        if my_date.weekday()==0 or my_date.weekday()==6 :
            my_date-=datetime.timedelta(days=1)
            continue
        valute_data = data['Valute']
        wr=csv.writer(file)
        for valute in valute_data.values():    
            if valute['CharCode'] == 'USD':
                wr.writerow((f"Дата: {data['Date']}").split(','))
                wr.writerow((f"{valute['Name']} курс: {valute['Value']}").split(','))
        my_date-=datetime.timedelta(days=1)
    