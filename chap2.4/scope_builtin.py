print(dir())
print(dir(__builtins__))

def incr(a, step=1):
    return a + step

print(incr(10))
print(incr(10,2))

def area(width, height):
    return width * height

print(area(height=10, width=20))

def varg(a, *arg):
    print(a, arg)

varg(1)
varg(1,2)
varg(1,2,3,4,5)
