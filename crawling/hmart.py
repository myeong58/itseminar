#!/usr/bin/python3

import urllib.request
import re
import pymysql

def get_hmart(jearyo,hm_url,hm_price,hm_name,hm_img):
	jearyo = urllib.parse.quote(jearyo,safe='')
	jearyo = urllib.parse.quote(jearyo,safe='')
	URL = 'http://www.homeplus.co.kr/app.search.HeaderSearch.ghs?comm=usr.header.search.basic4&search_query='
	URL = URL + jearyo
	req = urllib.request.urlopen(URL)
	text = req.read().decode("euc-kr")
	html = re.split("[\n\t]+",text)
	n = 0
	for i in html:
		if re.search("검색결과가 없습니다.",i):
			break
		if re.search("\"paging\"",i):
			break
		if re.search("<span class=\"ico\"",i):	
			line = re.split('([<>])',i)
			for k in line:
				name_1 = re.search("\d+\" alt=\"[\w\W]*\"",k)
				url_1 = re.search("jsGoodDetail\('\d+'",k)
				img_1 = re.search("img src=\"[\w\W]*.jpg",k)
				if (name_1):
					name_1 = re.sub("\d+\" alt=","",name_1.group())
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

