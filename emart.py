#!/usr/bin/python3

import urllib.request
import re

#만개의 레시피 오늘의 랭킹 top10 
emart = "http://www.ssg.com/search.ssg?target=all&query=식빵"

req = urllib.request.urlopen('http://www.ssg.com/search.ssg?target=all&query=%EC%8B%9D%EB%B9%B5')
text = req.read().decode("utf-8")
html = re.split("[\n\t]+",text)

#제품url
url = []
#섬네일
img = []
#제품이름
name = []
#가격
price = []
n = 0

for i in html:
	if i.find("blank clickable") > 0:	
		url_1 = re.search("/item/[\w\W]*=ssglist\"",i)
		url.append(url_1.group())
	elif i.find("notiTitle") > 0:
		name_1 = re.search('value="[\w\W]+',i)
		name_1 = re.sub("value=\"","",name_1.group())
		name_1 = re.sub("\">","",name_1)
		name.append(name_1)
	elif i.find("ssg_price") > 0:
		price_1 = re.search('\d+\W*\d*',i)
		price.append(price_1.group())
		n = n+1
	else:
		pass
	
	if n > 10:
		break

print(url)
print(name)
print(price)

