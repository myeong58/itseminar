#!/usr/bin/python3

import urllib.request
import re
import pymysql
from ranking import get_info
from material import get_mater
#from emart import get_emart
from hmart import get_hmart
from lmart import get_lmart

#랭킹 top10 url,섬네일, 메뉴이름
url = []; img=[]; name=[]
#재료
jaeryo=[[]*10 for i in range(10)]
#emart 
#em_url= []; em_price=[];em_name=[]; em_img = []
#hmart 
hm_url= []; hm_price=[];hm_name=[]; hm_img = []
#lmart 
lm_url= []; lm_price=[];lm_name=[]; lm_img = []
 

get_info(url, img, name)

for i,u in enumerate(url):
	get_mater(u,jaeryo[i])	
	
#SQL connection
conn = pymysql.connect(
	host='106.10.36.173',
	port=3306,
	user='Bo',
	passwd='Dhsmfdms?1',
	db='food'
)

#cursor생성
curs = conn.cursor()

#SQL문 실행
#jae = "INSERT ignore INTO JaeRyo (JR_Url,JR_Image,JR_Menu) SELECT (%s, %s, %s) from JaeRyo where not exists (select * from JaeRyo)"
jae = "INSERT ignore INTO JaeRyo (JR_Url,JR_Image,JR_Menu) VALUES (%s,%s,%s)"
#emart = "INSERT INTO E_Mart (EM_Jae,EM_Url,EM_Price,EM_Menu,EM_Image) VALUES (%s,%s,%s,%s,%s)"
hmart = "INSERT INTO H_Mart (HM_Jae,HM_Url,HM_Price,HM_Menu,HM_Image) VALUES (%s,%s,%s,%s,%s)"
lmart = "INSERT INTO L_Mart (LM_Jae,LM_Url,LM_Price,LM_Menu,LM_Image) VALUES (%s,%s,%s,%s,%s)"
Clear1 = "TRUNCATE TABLE JaeRyo"
Clear2 = "TRUNCATE TABLE JaeRyo2"
#Clear3 = "TRUNCATE TABLE E_Mart"
Clear4 = "TRUNCATE TABLE H_Mart"
Clear5 = "TRUNCATE TABLE L_Mart"

curs.execute(Clear1)
curs.execute(Clear2)
#curs.execute(Clear3)
curs.execute(Clear4)
curs.execute(Clear5)

for i in range(10): 
	curs.execute(jae,(url[i],img[i],name[i]))
	
	material = "INSERT INTO JaeRyo2 ("
	rang = ",".join(["JR_" + str(v+1) for v in range(len(jaeryo[i]))])
	ss = ",".join(["%s" for v in range(len(jaeryo[i]))])
	material = material + rang + ") VALUES ("  + ss + ")" 
	mat = tuple(jaeryo[i])

	curs.execute(material,(mat))


for y in range(10):
	for j in jaeryo[y]:
#		get_emart(j,em_url,em_price,em_name,em_img)
		get_hmart(j,hm_url,hm_price,hm_name,hm_img)
		get_lmart(j,lm_url,lm_price,lm_name,lm_img)
		for num in range(len(lm_name)):
			curs.execute(lmart,(j,lm_url[num],lm_price[num],lm_name[num],lm_img[num]))
		for num in range(len(hm_img)):
			curs.execute(hmart,(j,hm_url[num],hm_price[num],hm_name[num],hm_img[num]))
#		for num in range(len(em_url)):
#			curs.execute(emart,(j,em_url[num],em_price[num],em_name[num],em_img[num]))
#		em_url= []; em_price=[];em_name=[]; em_img = []
		hm_url= []; hm_price=[];hm_name=[]; hm_img = []
		lm_url= []; lm_price=[];lm_name=[]; lm_img = []

conn.commit()

conn.close()

