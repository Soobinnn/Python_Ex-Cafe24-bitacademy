# hello.py


def add(m, n):
    s = m
    s += n
    return s


def mymax(m, n):
    if m > n:
        return m
    else:
        return n


a = 1
b = 1
a = 2

if a > 1:
    print('big')
    print('big')

    for i in range(1, 10):
        print('-->', i)

print('end')