#!/usr/bin/python3

import urllib.request
import re
import pymysql

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
			url_1 = re.search("itemId=[\d]+",i)
			url_1 = re.sub("itemId=","",url_1.group())
			eurl = 'http://www.ssg.com/item/itemView.ssg?itemId='
			em_url.append(eurl+url_1)
		elif i.find("notiTitle") > 0:
			name_1 = re.search('value="[\w\W]+',i)
			name_1 = re.sub("value=\"","",name_1.group())
			name_1 = re.sub("\">","",name_1)
			em_name.append(name_1)
		elif i.find("ssg_price") > 0:
			price_1 = re.search('\d+\W*\d+',i)
			price_1 = re.sub(",","",price_1.group())
			em_price.append(price_1)
		elif i.find("notiImgPath") > 0:
			img_1 = re.search("//item.[\w\W]*.jpg",i)
			em_img.append(img_1.group())
			n = n+1
		else:
			pass
		if n > 10:
			break

#제품url
em_url = []
#제품이름
em_name = []
#가격
em_price = []
#이미지
em_img = []


a = '우유'

get_emart(a)

#print(em_url)
#print(em_name)
print(em_price)
#print(em_img)
'''
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
	curs.execute(sql,(em_url[i],em_price[i],em_name[i],em.img[i]))

curs.execute(sql2)
conn.commit()

conn.close()
'''	
