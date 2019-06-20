from urllib.parse import urlencode

from urllib.request import urlopen, Request

# GET
httpresponse = urlopen('http://www.example.com')
body = httpresponse.read()
print(httpresponse)
print(body)


# POST
data = {
    'email' : 'isb9082@naver.com',
    'password': '1234',
    'name':'임수빈'
}
data = urlencode(data).encode('utf-8')
print(data)

request = Request('http://www.example.com',data)
request.add_header('Content-Type', 'text/html')

httpresponse = urlopen(request)
print(httpresponse.read())

