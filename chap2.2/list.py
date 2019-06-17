# 리스트 생성과 연산

l = [1, 2, 'python']

print(l[-2], l[-1], l[0], l[1], l[2])
print(l[1:3])
print(1*2)
print(l+[3,4,5])
print(len(l))
print(2 in l)

del l[0]
print(l)

# 리스트는 변경 가능한 자료형 (Mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

# 슬라이스를 통한 치환
a = [1, 12, 123, 1234]

a[0:2] = [10,20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

a[2:3] = [30]
print(a)

# 슬라이스를 통한 삭제
a = [1, 12, 123, 1234]
a[1:2] = []
print(a)
a[0:] =[]
print(a)

# 슬라이스를 통한 삽입
a = [1, 12, 123, 1234]
a[1:1] = ['a']
print(a)

a[5:] = [12345]
print(a)

a[:0]=[-12,-1,0]
print(a)


# 리스트를 스택으로 사용하기
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

# 리스트를 큐로 사용하기
q = []
q.append(100)
q.append(200)
q.append(300)

print(q)

print(q.pop(0))
print(q.pop(0))

print(q)

# 리스트의 정렬
l = [1, 5, 3, 9, 8, 4, 2]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key=str)
print(l)

l.sort(key=int)
print(l)