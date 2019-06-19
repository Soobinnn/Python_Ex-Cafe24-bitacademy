import time
from datetime import datetime
import ssl
import sys
from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

def crawling_pelicana():
    results = []

    for page in range (1,5) :
        url =   'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        try :

            request = Request(url)
            # ssl._create_default_https_context = ssl._create_unverified_context()
            context = ssl._create_unverified_context()
            response = urlopen(request ,context=context)
            receive = response.read()
            html=receive.decode('utf-8',errors='replace')
            print(f'{datetime.now()}:success for request [{url}]')


        except Exception as e :
            print(f'{e}: {datetime.now()}',file=sys.stderr)
            # continue
        bs=BeautifulSoup(html,'html.parser')
        tag_table=bs.find('table',attrs={'class':'table'})
        tag_body=tag_table.find('tbody')
        tags_tr=tag_body.findAll('tr')

        #끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr :
            strings=list(tag_tr.strings)
            name=strings[1]
            address=strings[3]
            sidogu=address.split()[:2]
            results.append( (name,address)+tuple(sidogu) )

    # store
    table= pd.DataFrame(results,columns=['name','address','sido','gungu'])
    table.to_csv('__results__/pelicana.csv', encoding='UTF-8', mode='w', index=True)

    for t in results:
        print(t)


def crawling_nene():
    results = []

    for page in range(1, 5):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?page=%d&ex_select=1&ex_select2=&IndexSword=&GUBUN=A' % page
        try:

            request = Request(url)
            # ssl._create_default_https_context = ssl._create_unverified_context()
            context = ssl._create_unverified_context()
            response = urlopen(request, context=context)
            receive = response.read()
            html = receive.decode('utf-8', errors='replace')
            print(f'{datetime.now()}:success for request [{url}]')


        except Exception as e:
            print(f'{e}: {datetime.now()}', file=sys.stderr)
            # continue
        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('div', attrs={'class': 'shopWrap'})
        tag_body = tag_table.find('div', attrs={'class': 'shop'})
        tags_tr = tag_table.findAll('div', attrs={'class': 'shopInfo'})
        # print(tag_table)
        # print(tag_body)
        # print(tags_tr)

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[4]
            address = strings[6]
            sidogu = address.split()[:2]
            results.append((name, address) + tuple(sidogu))
            # print(strings)

            #print(address)
            #print(sidogu)


    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])
    table.to_csv('__results__/nene.csv', encoding='UTF-8', mode='w', index=True)

    for t in results:
        print(t)

def crawling_kyochon():
    for sido1 in range(1, 2):
        for sido2 in range(1, 2):
            url ='http://www.kyochon.com/shop/domestic.asp?sido1=0&sido2=0&txtsearch='
            crawler.crawling(url)

            # 끝검출

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class':'list'})
            tags_span = tag_ul.findAll('span', attrs={'class':'store'})

            for tag_span in tags_span:
                list(tag_span.strings)
                print(strings)

                name = strings[1]
                address = strings[3].replace('\r\n\t', '').strip()
                sidogu = address.split()[:2]

                print(name, address, sep=':')

def crawling_goobne():
    url=''

    # 첫 페이지 로딩
    wd = webdriver.Chrom('D:\python\chromedriver_win32\chromedriver.exe')
    wd.geturl(url)
    time.sleep(5)

    for page in range(1,2):
        # 자바스크립트 실행
        script = 'store.getList(%d)' % page
        wd.execute_script(scirpt)
        print(f'{datetime.now()}: success for request[{script}]')
        time.sleep(3)

        # 실행결과
        html = wd.page_source

        # parsing with bs4
        bs = BeautifulSoup(html,'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id':'store_list'})
        tags_tr = tag_tbody.findAlll('tr')

        # detect


if __name__ == '__main__' :
    # pelicana
    # crawling_pelicana()

    # crawling_nene()

