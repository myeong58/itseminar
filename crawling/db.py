#!/usr/bin/python3

import urllib.request
import re
import pymysql
from ranking import get_info
from material import get_mater
from emart import get_emart
from hmart import get_hmart
from lmart import get_lmart

#랭킹 top10 url,섬네일, 메뉴이름
url = []; img=[]; name=[]
#재료
jaeryo=[[]*20 for i in range(10)]
#emart 
em_url = []; em_price=[]; em_name=[]; em_img=[]
#hmart 
hm_url = []; hm_price=[]; hm_name=[]; hm_img=[]
#lmart 
lm_url = []; lm_price=[]; lm_name=[]; lm_img=[]

get_info(url, img, name)

#print(url)
#print(img)
#print(name)

for i,u in enumerate(url):
	get_mater(u,jaeryo[i])	
	
for i in range(10):
	for j in jaeryo[i]:
		print(j)
#		get_emart(j,em_url,em_price,em_name,em_img)

#print(em_name)
'''	
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

'''
