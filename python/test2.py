# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

date = input('원하는 날짜를 입력하세요(YYYYMMDD)')
for i in range(5):

    data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd='+ str(date) +'&hh=20&rtm=N&pg=' + str(i),headers=headers)

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

    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)

    #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
    # body-content > div.newest-list > div > table > tbody > tr:nth-child(33) > td.info > a.albumtitle.ellipsis
    for music in musics:
        title = music.select_one('td.info > a.title.ellipsis').text.strip()
        rank = music.select_one('td.number').text.split(' ')[0].strip()
        artist = music.select_one('td.info > a.artist.ellipsis').text
        album = music.select_one('td.info > a.albumtitle.ellipsis').text
        if title is not None:
            print (rank + " | " + title + " - " + artist + " | " + album)
