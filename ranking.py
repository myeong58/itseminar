#!/usr/bin/python3

import urllib.request
import re

#만개의 레시피 오늘의 랭킹 top10 
req = urllib.request.urlopen('http://www.10000recipe.com/ranking/list.html?type=hot')

text = req.read().decode("utf-8")
html = re.split("\n",text)

url = []
img = []
name = []

for i in html:
#	print(i)
	if i.find("ranking_today_in") > 0:
		url_1 = re.search('"/recipe/[0-9]*"',i)
		url.append(url_1.group())
		
		img_1 = re.search("http://recipe1.[\w\W]*.jpg",i)
		img.append(img_1.group())

		num = html.index(i)
		name_1 = re.sub("\s+","",html[num+5])
		name_1 = re.sub("</div>","",name_1)
		name.append(name_1)
	else:
		pass

print(url)
print(img)
print(name)

