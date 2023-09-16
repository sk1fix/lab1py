import requests
import json
import csv

url = "https://www.cbr-xml-daily.ru/archive/2022/09/08/daily_json.js"

response = requests.get(url)
data = json.loads(response.text)

with open('data.csv', 'w', newline='') as file:
    valute_data = data['Valute']
    wr=csv.writer(file)
    for valute in valute_data.values():    
        wr.writerow(f"Date: {data['Date']}")
        wr.writerow(f"{valute['Name']} курс: {valute['Value']}")