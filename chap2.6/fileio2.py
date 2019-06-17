f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('----'+text+'----')

#position 단위는 byte
pos = f.tell()
print(pos)

# (offset, from_what)
#          ,0(맨앞에서)


f.seek(16, 0)
text = f.read()
print(text)

# (offset, from_what)
#          ,2(맨끝에서)
# f.seek(10, 2)
# text = f.read()
# print(text)

# line 단위로 일기
linenum =0
f2 = open('fileio2.py', 'rt', encoding='utf-8')
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    linenum +=1
    print('{0}:{1}'.format(linenum, line))

f3 = open('fileio2.py','rt', encoding='utf-8')
lines = f3.readlines()
f3.close()

print(type(lines))
for linenum, line in enumerate(lines):
    print('{0}:{1}'.format(linenum, line), end='')

# 예외는 seek(0, 2) 끝으로 이동하는 경우
f.seek(0, 2)

f.seek(-5, 1)
data =f.read(3)
print(data)

# with ~ as
with open('fileio2.py', 'rt', encoding='utf-8') as f2:
    for linenum, line in enumerate(f2.readlines()):
        print('{0}:{1}'.format(linenum, line), end='')
