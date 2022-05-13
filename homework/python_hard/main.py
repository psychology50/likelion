'''
Question 1. Crawling

(1) 파싱의 정의 서술

(2) url = "<http://www.naver.com/>"
    response = requests.get(url)
    ① response object를 html 형태로 변환하여 soup 객체에 저장하는 코드 작성
    ② ①의 soup object를 활용해 네이버 홈페이지의 <title>태그를 출력하는 코드 작성
    ③ ①의 soup object를 활용해 네이버 홈페이지의 모든 메뉴를 크롤링(find)하시오.

(3) 빈칸을 채우시오
    #크롤링 결과(2-3)는 menus 객체에 저장함.
    file = ___("NaverMenu.txt", "__", encoding="UTF-8")

    for menu in menus:
        file.___(menu.____+"\n")
'''

# (1) 파싱 : 데이터 수집 기술. html, json과 같은 데이터 문자열에서 원하는 데이터만 분석 및 추출하는 것.

# (2)
import sys
import requests
from bs4 import BeautifulSoup

# ①
url = "http://www.naver.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# ②
print(soup.find("title"))
print(soup.select("title")) # list 형태로 반환
print(soup.head.title)

# ③
menus = soup.findAll("a", {"class":"nav"})

# (3)
try:
    file = open("NaverMenu.txt", "w", encoding="UTF-8")
except:
    sys.stderr.write("No file\n")
    exit(1)

for menu in menus:
    file.write(menu.get_text() + "\n")
file.close()



'''
Question 2. API
※ openweathermap - Air Pollution API 활용

Qualitative name    Pollutant concentration in μg/m3
    좋음                         0-30
    보통                        30-80
    나쁨                        80-150
  매우나쁨                         >151

대구의 미세먼지 농도(PM10) 값에 따른 Qualitative name을 출력하는 조건문 생성,
미세먼지 농도 값과 함께 출력하시오 (PM10 수치는 JSON에서 가져올 것)

- Daegu의 위도: *35.848987*, 경도:*128.72818*
- output : 미세먼지 농도 값(PM10), Qualitative name
'''
from datetime import datetime
import json

lat, lon = "35.848987", "128.72818"
apikey = "c226b085b5f8eb142932949814873d25"
lang = "kr"

api = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apikey}"

result = requests.get(api)
data = json.loads(result.text)
today = data["list"][0]["components"]["pm10"]

print(datetime.today().strftime("%Y년 %m월 %d일의 미세먼지 농도입니다."))

if today > 151:
    output = "매우나쁨"
elif 150 >= today > 80:
    output = "나쁨"
elif 80 >= today > 30:
    output = "보통"
elif 30 >= today >= 0:
    output = "좋음"

print(f"미세먼지 농도 : {today}, {output}입니다.", end = ' ')
