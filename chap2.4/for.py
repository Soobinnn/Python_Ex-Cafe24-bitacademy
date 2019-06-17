# list, range 객체를 사용하는 for문
a = ['cat','cow','tiger']

for animal in a:
    print(animal)

for x in range(10):
    print(x, end=" ")

# 복합 자료형을 사용하는 for문
l = [('둘리', 10), ('마이콜',20), ('도우넛',30)]

for data in l:
    print('이름:%s 나이:%d' % data)

for name, age in l:
    print('이름:{0},나이:{1}'.format(name, age))

l = ['red', 'orange', 'yellow', 'green', 'blue']
for index, color in enumerate(l):
    print(index, color)

for i in range(10):
    if i > 5:
        break
    print(i,end='')


