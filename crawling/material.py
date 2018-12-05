#!/usr/bin/python3

import urllib.request
import re


jaeryo = []

def get_mater(url):
	u = 'http://www.10000recipe.com'
	u = u + url
	req = urllib.request.urlopen(u)
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

#get_mater('/recipe/6880142')
#print(jaeryo)
#get_mater('/recipe/6847470')
get_mater('/recipe/6864080')
print(jaeryo)
