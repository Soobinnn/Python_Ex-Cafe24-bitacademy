# write test
f = open('test.txt', 'w', encoding='utf-8')
write_size = f.write('안녕하세요\n임수빈 입니다.')
print(write_size)
f.close()


# read test
f = open('test.txt','r', encoding='utf-8')
text = f.read()
print(text)
f.close()


# binary mode :  b
f = open('test2.txt', 'wb')
writesize = f.write(bytes('안녕하세요\n파이썬입니다.', encoding='utf-8'))
print(writesize)
f.close()


#read test
open('test.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)


# binary read: copy file
fsrc = open('python png', 'rb')
data = fsrc.read()
fsrc.close()

print(type(data))
fdest = open('python2.png', 'wb')
fdest.write(data)
fdest.close()
