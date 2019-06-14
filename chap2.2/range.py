seq = range(10)
print(seq, type(seq))
print(list(seq[5:]))
print(len(seq))

for i in seq:
    print(i, end=' ')
else:   #정상 종료 시
    print()

for i in range(0, -10, -1):
    print(i, end=' ')
else:
    print()

for i in range(0, 10, 2):
    print(i, end=' ')
else:
    print()

print('ok')

index = 0
for color in ['red', 'blue', 'black', 'white']:
    print("{0}:{1}".format(index, color))
    index += 1

for index, color in enumerate(['red', 'blue', 'black', 'white']):
    print("{0}:{1}".format(index, color))


