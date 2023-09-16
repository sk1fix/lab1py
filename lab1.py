import requests
import json

url = "https://www.cbr-xml-daily.ru/archive/2022/09/08/daily_json.js"

response = requests.get(url)
data = json.loads(response.text)


valute_data = data['Valute']
for valute in valute_data.values():    
    print(f"Date: {data['Date']}")
    print(f"{valute['Name']} rate: {valute['Value']}")
