from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET / HTTP/1.1
# 200 OK
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)

if resp.status == 200:
    data = resp.read()
    print(body, type(body))

# 실패
# GET / HTTP/1.1
# 404 File Not Found
conn.request('GET', '/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason)
