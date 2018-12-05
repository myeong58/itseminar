#!/usr/bin/python3

import urllib.request
import re
import pymysql

#제품url
m_url = []
#제품이름
m_name = []
#가격
m_price = []

def get_emart(jearyo):
	jearyo = urllib.parse.quote(jearyo,safe='')
	URL = 'http://www.ssg.com/search.ssg?target=all&query='
	URL = URL + jearyo
	req = urllib.request.urlopen(URL)
	text = req.read().decode("utf-8")
	html = re.split("[\n\t]+",text)
	n = 0
	for i in html:
		if i.find("blank clickable") > 0:	
			url_1 = re.search("/item/[\w\W]*=ssglist\"",i)
			m_url.append(url_1.group())
		elif i.find("notiTitle") > 0:
			name_1 = re.search('value="[\w\W]+',i)
			name_1 = re.sub("value=\"","",name_1.group())
			name_1 = re.sub("\">","",name_1)
			m_name.append(name_1)
		elif i.find("ssg_price") > 0:
			price_1 = re.search('\d+\W*\d+',i)
			m_price.append(price_1.group())
			n = n+1
		else:
			pass
		if n > 10:
			break

a = '당근'

get_emart(a)

#print(m_url)
#print(m_name)
print(m_price)

conn = pymysql.connect(
	host='localhost',
	port=3306,
	user='Bo',
	passwd='Dhsmfdms?1',
	db='food'
)

curs = conn.cursor()

sql = "INSERT INTO E_Mart (EM_Url,EM_Price,EM_Menu) VALUES (%s,%s,%s)"
sql2 ="SELECT DISTINCT * FROM E_Mart"

for i in range(10):
	curs.execute(sql,(m_url[i],m_price[i],m_name[i]))

curs.execute(sql2)
conn.commit()

conn.close()
	
