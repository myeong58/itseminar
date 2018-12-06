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
'''
u=[];p=[];n=[];m=[];i=[]

get_emart('dd',u,p,n,i)
print(u,p,n,m,i)
get_emart('우유',u,p,n,i)
print(u,p,n,m,i)

'''
