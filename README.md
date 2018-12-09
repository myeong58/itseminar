 IT-Seminar
===============

# WHAT IS THIS?

- 요리하는 자취생들을 위한  레시피 및 가격비교  사이트

레시피 사이트의 오늘의 랭킹 TOP10의 정보와 재료 정보를 가져와
홈플러스, 이마트, 롯데마트 3개의 온라인 쇼핑몰에서 가격비교를 해주는 사이트 입니다.

> crawling.
> - ranking:
> 
>	만개의 레시피의 오늘의 Top10 레시피 정보 크롤링.	
> - material:
> 
>	각 레시피에서 재료정보 크롤링.	
> - emart, hmart, lmart:	
> 
> 	각 마트에서 재료에 대한 상위 10개의 제품정보 크롤링.	
> - db:
> 
> 	크롤링해온 정보를 DB로 전송. 	
 

# Environment

* Ubuntu 18.04
* Apache2
* MySQL 5.7

* Python3
* PHP 7.0

# Modules

    `$ sudo apt install python3`    	
	
    `$ sudo apt install python3-pip`    	
	
    `$ pip install pymysql`    	
	
    `$ pip install fake-useragent`     	
	
    `$ pip install urllib3` 
    

# Site

<http://106.10.36.173/index.php>

# Target Site

<http://www.10000recipe.com/ranking/list.html?type=hot>

<http://emart.ssg.com/>
<http://www.homeplus.co.kr/>
<http://www.lottemart.com/>
