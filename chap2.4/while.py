count = 1
while count < 11:
    print(count, end = '')
    count +=1
else:
    print('')

# 1 ~ 10 까지 합
hap, i = 0, 1
while i <= 10:
    hap += i
    i += 1
print('합: {0}'.format(hap))

i = 0
while i < 10:
    i += 1
    if i < 5:
        continue
    print(i, end='')
    if i > 10:
        break
else:
    print('else block')

print('done')

i = 0
while True:
    print(i)
    if i > 5:
        break
    i += 1