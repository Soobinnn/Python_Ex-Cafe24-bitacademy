i = 0

for value in ['red', 'yellow', 'blue', 'white', 'gray']:
    print('{0}:{1}'.format(i,value))
    i += 1

# 비교 : enumberate 함수를 사용했을 때

for i, value in enumerate(['red', 'yellow', 'blue', 'white', 'gray']):
    print('{0}:{1}'.format(i, value))