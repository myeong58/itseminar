 IT-Seminar
===============

# <What Today's Food?>

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
> - database:
> 
>      크롤링한 데이터들을 각 마트별 테이블에 저장하고 레시피의 재료 테이블에 각각 저장.
> - web:
>
>      Query문을 이용하여 크롤링한 데이터들을 추출하여 웹페이지를 통해 시각화.

 

# Environment

* Ubuntu 18.04
* Apache2
* MySQL 5.7

* Python3
* PHP 7.0

# Installation

> Ubuntu 18.04에 LAMP ( Apache2, PHP5 / PHP7) 설치하는 방법은 아래의 링크를 참고해 주세요.
* https://webnautes.tistory.com/1185 

> MySql 5.7의 세부적인 설정은 아래의 링크를 참고해 주세요.
* http://all-record.tistory.com/183


# Modules

    `$ sudo apt install python3`    	
	
    `$ sudo apt install python3-pip`    	
	
    `$ pip install pymysql`    	
	
    `$ pip install fake-useragent`     	
	
    `$ pip install urllib3`

# OverView

![system](https://raw.githubusercontent.com/myeong58/itseminar/master/ppt/system.png)
    
# DataBase Table  

![dbtable](https://raw.githubusercontent.com/myeong58/itseminar/master/ppt/dbtable.PNG)

# Site

<http://106.10.36.173/index.php>

# Target Site

* <http://www.10000recipe.com/ranking/list.html?type=hot>

* <http://emart.ssg.com/>
* <http://www.homeplus.co.kr/>
* <http://www.lottemart.com/>
