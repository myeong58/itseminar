#!/usr/bin/python3

import urllib.request
from urllib.request import HTTPError
import re
from fake_useragent  import UserAgent
from random import *
import time

def get_emart(jearyo,em_url,em_price,em_name,em_img):
	time.sleep(randint(0,10))
	jearyo = urllib.parse.quote(jearyo,safe='')
	URL = 'http://www.ssg.com/search.ssg?target=all&query='
	URL = URL + jearyo
	try:
		ua = UserAgent()
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-agent', ua.random)]
		urllib.request.install_opener(opener)
		req = urllib.request.urlopen(URL)
	except HTTPError as e:
#		time.sleep(randint(10,30))
		print(e)
	finally:
		text = req.read().decode("utf-8")
		html = re.split("[\n\t]+",text)
		n = 0
		for num,i in enumerate(html):
			ex = re.search("검색결과가 없습니다.",i)
			u = re.search("\"thmb\"",i)
			na = re.search("notiTitle",i)
			p = re.search("ssg_price",i)
			im = re.search("notiImgPath",i)
			if re.search("pager",i):
				break
			if ex:
				break
			if n > 5:
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
