# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다

name = "길동"
age = 40

print("name: " + name + ", age:" + format(age, "d"))
print("name:" + format(name, "s") + ",age:" + format(age, "d"))

# 튜플을 이용한 문자열 포메팅
print('# 튜플을 이용한 문자열 포메팅=======================')

f = 'name:%s,age:%d'

print(f % ('둘리', 20))
print(f % ('또치', 10))
print(f % ('도우넛', 30))

# 딕션너리를 이용한 포메팅
print('# 딕션너리를 이용한 포메팅=======================')

f = 'name:%(name)s, age: %(age)d'
print(f)

print(f % {'name': '둘리', 'age': 20})
print(f % {'name': '또치', 'age': 10})
print(f % {'name': '도우넛', 'age': 30})

# 대소문자 관련 메소드
print('# 대소문자 관련 메소드=======================')

s = 'i like Python'

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 검색관련 메소드
print('# 검색관련 메소드=======================')

s = 'I Like Python. I Like Java Also'

print(s.count('Like'))
print(s.find('Like', 5))
print(s.find('JS'))
print(s.rfind('Like'))

# print(s.index('JS')
print(s.rindex('Like'))

print(s.startswith('I Like'))
print(s.startswith('Like', 2))
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))

# 편집과 치환 메소드
print('# 편집과 치환 메소드=======================')
s = 'spam and ham'
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s = '<><abc><><defg><><>'
print(s.strip('<>'))

s = 'Hello Java'
print(s.replace('Java', 'Python'))

# 정렬 메소드
print('# 정렬 메소드=======================')

s = 'king and queen'

print(s.center(60))
print(s.center(60, '-'))
print(s.ljust(60, '-'))
print(s.rjust(60, '-'))

# 분리와 결합 메소드
print('# 분리와 결합 메소드=======================')

s = 'spam and ham'
t = s.split();
print(t)
t = s.split('and')
print(t)

s2 =":".join(t)
print(s2)

s3 = "one:two:three:four:five"
print(s3.split(':',2))
print(s3.rsplit(':',2))

lines ="1st line " \
       "2nd line  " \
       "2nd line  " \
       "4th line  " \
       "5 line " \
       "6 line"
print(lines.splitlines());

# 판별 메소드
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234'.isalpha())
print('abcd'.isdigit())

print('abcd'.islower())
print('ABCD'.isupper())

print('\n\n'.isspace())
print(''.isspace())
print(''.isspace())

print('20'.zfill(5))
print('1234'.zfill(5))

# 서식 메소드
f = 'name: {}, age: {}'
print(f)
print(f.format("둘리", 10))

print('name:{0},age:{1}'.format('둘리',10))
print('name:{1},age:{0}'.format(30, '마이콜'))

print('{:3}의 제곱근은 {:.5}입니다.'.format(2, 2**0.5))
print('{1:03}의 제곱근은 {0:.5}입니다.'.format(2**0.5,2))

f = "name: {name}, age: {age}"
print(f.format_map({'name':'도우넛','age':10}))