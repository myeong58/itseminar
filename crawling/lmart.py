#!/usr/bin/python3

import urllib.request
import re
import pymysql
import sys

def get_lmart(jearyo,lm_url,lm_price,lm_name,lm_img):
	jearyo = urllib.parse.quote(jearyo,safe='')
	URL = 'http://www.lottemart.com/search/search.do?searchTerm='
	URL = URL + jearyo
	req = urllib.request.urlopen(URL)
	text = req.read().decode("utf-8")
	html = re.split("[\n\t]+",text)
	n = 0
	for i,x in enumerate(html):
		l = re.search("prod-name",x)
		p = re.search("num-n",x)
		m = re.search("wrap-thumb",x)
		if l:
			#url 추출
			lm_url_1 = re.search("Detail\('C\d+', '\d+'",html[i+2])
			lm_url_1 = re.split("[']",lm_url_1.group())	
			lm_url_1 = 'http://www.lottemart.com/product/ProductDetail.do?CategoryID=' + lm_url_1[1] + '&ProductCD=' + lm_url_1[3]	
			lm_url.append(lm_url_1)

			#제품명
			lm_name_1 = re.sub("</a>","",html[i+3])
			lm_name.append(lm_name_1)
		
		if p:
			#가격	
			lm_price_1 = re.search("\d+\W*\d+",html[i])
			lm_price_1 = re.sub(",","",lm_price_1.group())
			lm_price.append(lm_price_1)
		if m:
			lm_img_1 = re.search("http://[\w\W]+.jpg",html[i+2])
			lm_img.append(lm_img_1.group())
			n = n+1
			if n > 10:
				break
