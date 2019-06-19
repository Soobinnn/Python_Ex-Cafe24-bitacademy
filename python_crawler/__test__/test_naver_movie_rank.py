#       proc1         proc2
# data ------> data1 ------> data2
# html -> proc ->  divs -> stroe -> X
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from python_crawler.__test__ import crawler


def ex01():
    # request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    response = urlopen(request)
    html = response.read().decode('cp949')
    print(html)

    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())
    divs = bs.findAll('div', attrs={'class': 'tit3'})
    # print(divs)
    return divs

def proc_naver_movie_rank(data):
    #output(store)
    for index, div in enumerate(data):
        print(index+1, div.a.text, div.a['href'], sep=':')

def ex02():
    print('!!!!!!!')
    # fetch
    crawler.crawling(
        url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        encoding = 'cp949', proc = proc_naver_movie_rank)

    # processing
    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class':'tit3'})

__name__ == '__main__' and not \
    ex01() and not \
    ex02()

