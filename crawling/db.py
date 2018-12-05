#!/usr/bin/python3

import urllib.request
import re
import pymysql

def get_info(url, img, name):
	#만개의 레시피 오늘의 랭킹 top10 
	URL = "http://www.10000recipe.com/ranking/list.html?type=hot"
	req = urllib.request.urlopen(URL)
	text = req.read().decode("utf-8")
	html = re.split("\n",text)

	for i in html:
		#top10이 있는 부분 탐색	
		if i.find("ranking_today_in") > 0:
			#url 파싱
			url_1 = re.search('"/recipe/[0-9]*"',i)
			url.append(url_1.group())
		
			#이미지 파싱
			img_1 = re.search("http://recipe1.[\w\W]*.jpg",i)
			img.append(img_1.group())
			
			#메뉴이름 파싱
			num = html.index(i)
			name_1 = re.sub("\s+","",html[num+5])
			name_1 = re.sub("</div>","",name_1)
			name.append(name_1)
		else:
			pass

#랭킹 top10 url
url = []
#섬네일
img = []
#메뉴이름
name = []


get_info(url, img, name)

#print(url)
#print(img)
#print(name)
	
#SQL connection
conn = pymysql.connect(
	host='localhost',
	port=3306,
	user='Bo',
	passwd='Dhsmfdms?1',
	db='food'
)

#cursor생성
curs = conn.cursor()

#SQL문 실행
sql = "INSERT INTO JaeRyo (JR_Url,JR_Image,JR_Menu) VALUES (%s,%s,%s)"
for i in range(10): 
	curs.execute(sql,(url[i],img[i],name[i]))

conn.commit()

conn.close()


