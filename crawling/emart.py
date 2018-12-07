#!/usr/bin/python3

import urllib.request
from urllib.request import HTTPError
import re
import pymysql

def get_emart(jearyo,em_url,em_price,em_name,em_img):
	jearyo = urllib.parse.quote(jearyo,safe='')
	URL = 'http://www.ssg.com/search.ssg?target=all&query='
	URL = URL + jearyo
	try:
		req = urllib.request.urlopen(URL)
	except HTTPError as e:
		pass
	else:
		text = req.read().decode("utf-8")
		html = re.split("[\n\t]+",text)
		n = 0
		for num,i in enumerate(html):
			ex = re.search("검색결과가 없습니다.",i)
			u = re.search("\"thmb\"",i)
			na = re.search("notiTitle",i)
			p = re.search("ssg_price",i)
			im = re.search("notiImgPath",i)
			if ex:
				break
			if n > 10:
				break
			if u:	
				url_s = re.split("\"",html[num+1])
				url_1 = "www.ssg.com" + url_s[1]
				em_url.append(url_1)
			elif na:
				name_1 = re.search('value="[\w\W]+',i)
				name_1 = re.sub("value=\"","",name_1.group())
				name_1 = re.sub("\">","",name_1)
				em_name.append(name_1)
			elif p:
				price_1 = re.search('\d+\W*\d+',i)
				price_1 = re.sub(",","",price_1.group())
				em_price.append(price_1)
			elif im:
				img_1 = re.search("//item.[\w\W]*.jpg",i)
				em_img.append(img_1.group())
				n = n+1
			else:
				pass
'''
q=[];w=[];e=[];r=[]
get_emart('고추장',q,w,e,r)
print(q)
print(w)
print(e)
print(r)

'''
