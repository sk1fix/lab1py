import requests

from bs4 import BeautifulSoup

url='https://www.cbr-xml-daily.ru/archive/2022/09/08/daily_json.js'

html_text = requests.get(url)