from datetime import datetime
import ssl
import sys
from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup

def crawling(url='', encoding='utf-8', proc1= lambda data: data,proc2= lambda data: data, err=print(f'{e}: {datetime.now()}', file=sys.stderr)):
    results = []

    for page in range(1, 5):
        url = 'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        try:
            request = Request(url)
            # ssl._create_default_https_context = ssl._create_unverified_context()
            context = ssl._create_unverified_context()
            response = urlopen(request, context=context)
            receive = response.read()
            result =proc2(proc1(receive.decode('utf-8', errors='replace')))

            # if proc is not None:
            #     result = proc(html)
            #  else:
            #     result = html proc is not None else proc(html)
            # print(f'{datetime.now()}:success for request [{url}]')

            return result

        except Exception as e:
            print(f'{e}: {datetime.now()}', file=sys.stderr)
            # continue
        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': 'table'})
        tag_body = tag_table.find('tbody')
        tags_tr = tag_body.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]
            results.append((name, address) + tuple(sidogu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])
    table.to_csv('__results__/pelicana.csv', encoding='UTF-8', mode='w', index=True)

    for t in results:
        print(t)

