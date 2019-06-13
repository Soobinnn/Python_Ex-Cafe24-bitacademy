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
