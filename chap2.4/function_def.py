def dummy():
    pass

def my_function():
    print("Hello World")

def times(a, b):
    return a * b

def none():
    return

dummy()
my_function()
print(times(10, 10))
print(none())

t = times
print(t(100, 100))
print(t, times, sep=',')

