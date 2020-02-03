# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup



# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


data = requests.get('https://www.cnbc.com/nasdaq-100/',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')


#############################
# (입맛에 맞게 코딩)
#############################

#해당되는 여러 대상 리스트로 가져오기
#result = soup.select('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
#해당되는 하나의 대상을 가져옴
#result = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

stocks = soup.select('#MarketData-MarketsSectionTable-3 > section > div > div > div > div > table > tbody > tr')#MarketData-MarketsSectionTable-3 > section > div:nth-child(1) > div > div > div > table > tbody > tr:nth-child(1)
#MarketData-MarketsSectionTable-3 > section > div:nth-child(1) > div > div > div > table > tbody > tr:nth-child(1)
test = soup.select_one('#MarketData-MarketsSectionTable-3 > section > div > div > div > div > table > tbody ')
print (test)
for stock in stocks:
    symbol = stock.select_one('td.BasicTable-symbol').text
    # rank = music.select_one('td.number').text.split(' ')[0].strip()
    # artist = music.select_one('td.info > a.artist.ellipsis').text
    # album = music.select_one('td.info > a.albumtitle.ellipsis').text
    print (symbol)
    if stock is not None:
        print (symbol)
        # print (rank + " | " + title + " - " + artist + " | " + album)
