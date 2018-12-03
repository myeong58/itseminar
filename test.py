#!/usr/bin/python3

import requests
import re
from bs4 import BeautifulSoup

#만개의 레시피 오늘의 랭킹 top10 
req = requests.get('http://www.10000recipe.com/ranking/list.html?type=hot')
html = req.text
soup = BeautifulSoup(html,'html.parser')
#top 10 html 태그
my_titles = soup.select('.ranking_today_in')

#랭킹 top10 링크
url = []
#업로더
name = []
#메뉴
food = []

text = []
for title in my_titles:
	url.append(title.get('href'))	
	text = re.split('\s*',title.text)
	name.append(text[2])
	food.append(' '.join(text[3:]))

print(food)
print(name)
