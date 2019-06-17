x = 1
def func(a):
    return a + x

print(func(10))

x = 1
def func2(a):
    x = 2
    return a + x

print(func2(10))
print(x)

g = 1
def func3(a):
    global g
    g = 3
    return a + g

print(func3(10))
print(g)
