import requests
# requests.get(url, params=None, **kwargs) -> Return object
from bs4 import BeautifulSoup
# BeautifulSoup(data, Parsing)
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#정보를 가져오려는 사이트에 내가 로봇이 아님을 보여줌
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
#print(requests.get(url)) # 200 == success

response = requests.get(url, headers=headers)

#print(response.text) // output : html info (class 'str')
#print(BeautifulSoup(response.text, 'html.parser')) // same value, diffent type (class 'bs4.BeautifulSoup')

soup = BeautifulSoup(response.text, 'html.parser')

'''
file = open("daum.html", "w") // write mod
file.write(response.text)
file.close()
'''

search_rank_file = open("rankresult.txt", "w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

results = soup.findAll("a", "link_favorsch") # 해당 클래스에 속한 a태그만 가져옴.
rank = 1
for result in results:
    search_rank_file.write(str(rank) + "위 : " + result.get_text() + "\n")
    #print(rank, "위 : ", result.get_text(), "\n")
    rank += 1

