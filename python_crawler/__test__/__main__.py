import ssl
import sys
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def crawling_pelicana():
    results = []

    for page in count(5):
        url =''''https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d''' %page
        try:
            request = Request(url)
            # ssl._create_default_https_context = ssl._create_unverified_context()
            context = ssl._create_unverified_context()
            response = urlopen(request, context=context)

            receive = response.read()
            html = receive.decode('utf-8', errors='replace')

            print(f'{datetime.now()}: success for request [{url}]')
        except Exception as e:
            print(f'{e} : {datetime.now()}', file=sys.stderr )
            continue

        bs=BeautifulSoup(html,'html.parser')

        print(bs)
        tag_table = bs.find('table', attrs={'class':'table'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

    # 끝 검출

    for tag_tr in tags_tr:
        strings = list(tag_tr.strings)
        name = strings[1]
        address = strings[3]
        sidogu = address.split()[:2]
        print('======================')

    for t in results:
        print(t)
        t = (name, address) + tuple(sidogu)
        results.append(t)

def crawling_nene():
    pass

if __name__ == '__main__':
    # pelicana
    crawling_pelicana()

    # nene 과제
    # crawling_nane()