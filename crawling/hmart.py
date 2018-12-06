#!/usr/bin/python3

import urllib.request
import re
import pymysql

def get_hmart(jearyo):
	jearyo = urllib.parse.quote(jearyo,safe='')
	jearyo = urllib.parse.quote(jearyo,safe='')
	URL = 'http://www.homeplus.co.kr/app.search.HeaderSearch.ghs?comm=usr.header.search.basic4&search_query='
	URL = URL + jearyo
	req = urllib.request.urlopen(URL)
	text = req.read().decode("euc-kr")
	html = re.split("[\n\t]+",text)
	n = 0
	for i in html:
		if re.search("<span class=\"ico\"",i):	
			line = re.split('([<>])',i)
			for k in line:
				name_1 = re.search("alt=\"[\w\W]*\"",k)
				url_1 = re.search("jsGoodDetail\('\d+'",k)
				img_1 = re.search("img src=\"[\w\W]*.jpg",k)
				if (name_1):
					name_1 = re.sub("alt=","",name_1.group())
					hm_name.append(name_1)
				if(url_1):
					url_1 = re.search("\d+",url_1.group())
					h_url = 'http://www.homeplus.co.kr/app.product.GoodDetail.ghs?comm=usr.detail&good_id='
					hm_url.append(h_url+url_1.group())
				if(img_1):
					img_1 = re.sub("img src=\"","",img_1.group())
					hm_img.append(img_1)
		elif re.search("cost",i):
			price_1 = re.search('\d+\W*\d+',i)
			price_1 = re.sub(",","",price_1.group())
			hm_price.append(price_1)
			n = n+1
		else:
			pass
		if n > 10:
			break

#제품url
hm_url = []
#제품이름
hm_name = []
#가격
hm_price = []
#이미지
hm_img = []

a = '우유'
get_hmart(a)
#print(hm_url)
#print(hm_name)
print(hm_price)
#print(hm_img)

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
	curs.execute(sql,(m_url[i],m_price[i],m_name[i]))

curs.execute(sql2)
conn.commit()

conn.close()
'''	
