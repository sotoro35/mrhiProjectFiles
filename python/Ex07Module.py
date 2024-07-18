#1) 표준 모듈 : 파이썬에 기본으로 내장된 모듈(라이브러리) - 별도 설치 필요 없음
#2) 외부 모듈 : 외부에서 만든 모듈(라이브러리) - 별도 설치 필요 pip 로 다운로드


# 1.math 모듈
import math

print( math.sin(1))
print( math.floor(3.7))
print( math.ceil(3.7))
print( round(3.7))

import math as m
print( m.pow(4,2) )

from math import floor
print(floor(3.1))


# 2. random 모듈
import random

print( random.random())
print(random.randrange(10)) # 0 ~ 9 까지
print(random.randrange(5,16)) # 5 ~ 15 까지


aaa=[1,2,3,4,5]
print( random.choice(aaa))
print( random.sample(aaa,3))


lotto= list( range(1,46))
print( lotto )

nums= random.sample(lotto, 6)
print(nums)

nums.sort()
print( nums )


# open api 요청
from urllib import request
url= request.urlopen("http://mrhi2024.dothome.co.kr")
data= url.read()

print(data)
print("=================")


#외부모듈 -- html파서.. 기상청 RSS
url= request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")


from bs4 import BeautifulSoup

soup= BeautifulSoup(url,"xml")
print("지역개수:" , len(soup.select("location")))
print()

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    



