results = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = n * n
    results.append(result)

print(results)

results = [n*n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(results)

# 문자열 리스트에서 길이가 2이하인 문자열 리스트
strings = ['a', 'as', 'bar', 'car', 'dove', 'python']
strings = ['[' + s + ']' for s in strings if len(s) <= 2]
print(strings)

# 1-100 사이의 수준에서 짝수 리스트
evens = [n for n in range(1, 101) if n % 2 == 0]
print(evens)

# set comprehension
strings = ['a', 'as', 'bar', 'car', 'dove', 'python']
strings = {s for s in strings if len(s) <= 2}
print(strings)

# 문자열 길이를 set으로 저장하기
strings = ['a', 'as', 'bar', 'car', 'dove', 'python']
strlenggths = {len(s) for s in strings}
print(strings)

# dict comprehension
strings = ['a', 'bar', 'car', 'dove', 'as', 'python']
d = {s: len(s) for s in strings}
print(d)

#
# 369
#

#for t in(n, '짝'*(str(n).count('3')+str(n).count('6')+str(n).count('9'))):
#    for n in range(1, 1000) if '3' in str(n) or '6' in str(n) or '9' in str(n)
#        print('%s: %s' %t)


# 문자열 리스트에서 길이가 2 이하인 문자열 리스트 만들기
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = [s for s in strings if len(s) <= 2]
print(strings)

# 1~ 100 사이의 수중에 짝수 리스트 만들기
evens = [i for i in range(1, 101) if i % 2 == 0]
print(evens)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = [len(s) for s in strings]
print(lens)

lens = {len(s) for s in strings}
print(lens)

# 문자열 리스트에서 문자열과 문자열 길이를 함께 dict로 저장
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
dicts = {s: len(s) for s in strings}
print(dicts)