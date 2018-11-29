#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.10000recipe.com/ranking/list.html?type=hot')
html = req.text
soup = BeautifulSoup(html,'html.parser')

my_titles = soup.select('.ranking_today_in')

url = []
text = []
for title in my_titles:
	url.append(title.get('href'))	
	text.append(title.text)

print(text)
