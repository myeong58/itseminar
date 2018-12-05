#!/usr/bin/python3

import urllib.request
import re


jaeryo = []

def get_mater(URL):
	req = urllib.request.urlopen(URL)
	text = req.read().decode("utf-8")
	html = re.split("[\n\t]+",text)
	#print(html)

	for i in html:
		if re.search("ready_ingre3",i):
			num = html.index(i) + 1 
			while(html[num].find("</div>") < 0):
				if html[num].find("<li>") > 0:
					jaeryo_1= re.search("<li>[\w\W]+\s\s+",html[num])
					jaeryo_1 = re.sub("<li>","",jaeryo_1.group())
					jaeryo_1 = re.sub("\s+","",jaeryo_1)
					jaeryo.append(jaeryo_1)
				num = num+1
			break	
		else:
			pass

uuu = 'http://www.10000recipe.com/recipe/6864080'
#print(type(uuu))
get_mater(uuu)
print(jaeryo)
