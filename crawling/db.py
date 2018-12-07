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
jaeryo=[[]*10 for i in range(20)]
#emart 
em_url= [[]*10 for i in range(20)]; em_price=[[]*10 for i in range(20)];
em_name=[[]*10 for i in range(20)]; em_img = [[]*10 for i in range(20)]
#hmart 
hm_url =[[]*10 for i in range(20)]; hm_price=[[]*10 for i in range(20)];
hm_name=[[]*10 for i in range(20)]; hm_img = [[]*10 for i in range(20)]
#lmart 
lm_url =[[]*10 for i in range(20)]; lm_price=[[]*10 for i in range(20)];
lm_name=[[]*10 for i in range(20)]; lm_img = [[]*10 for i in range(20)]

get_info(url, img, name)

for i,u in enumerate(url):
	get_mater(u,jaeryo[i])	
	
#print(url)
#print(img)
#print(name)
#print(jaeryo)
 
#for i in range(10):
for k,j in enumerate(jaeryo[0]):
	print(j,'\n')
	get_emart(j,em_url[k],em_price[k],em_name[k],em_img[k])
	print(em_url[k],'\n',em_price[k],'\n',em_name[k],'\n',em_img[k])
##	get_hmart(j,hm_url[k],hm_price[k],hm_name[k],hm_img[k])
#	get_lmart(j,lm_url[k],lm_price[k],lm_name[k],lm_img[k])
'''
			
print(em_url)
print("\n")
print(em_price)
print('\n')
print(em_name)
print('\n')
print(em_img)


print('\n')
print('\n')

print(hm_url)
print('\n')
print(hm_price)
print('\n')
print(hm_name)
print('\n')
print(hm_img)

print('\n')
print('\n')

print(lm_url)
print('\n')
print(lm_price)
print('\n')
print(lm_name)
print('\n')
print(lm_img)
'''
'''	
#SQL connection
conn = pymysql.connect(
	host='localhost',
	port=3306,
	user='root',
	passwd='M8rYM4A6ignm',
	db='food'
)

#cursor생성
curs = conn.cursor()

#SQL문 실행
jaeryo = "INSERT INTO JaeRyo (JR_Url,JR_Image,JR_Menu) VALUES (%s,%s,%s)"
emart = "INSERT INTO E_Mart (EM_Url,EM_Image,EM_Menu,EM_Image) VALUES (%s,%s,%s,%s)"
hmart = "INSERT INTO H_Mart (HM_Url,HM_Image,HM_Menu,HM_Image) VALUES (%s,%s,%s,%s)"
jmart = "INSERT INTO L_Mart (LM_Url,LM_Image,LM_Menu,LM_Image) VALUES (%s,%s,%s,%s)"

for i in range(10): 
	curs.execute(sql,(url[i],img[i],name[i]))

conn.commit()

conn.close()

'''
