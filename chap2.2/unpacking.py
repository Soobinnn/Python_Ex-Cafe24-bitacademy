t = 10, 20, 30, 'python'
print(t)
print(type(t))

# unpacking tuple
a, b, c, d = t
print(a, b, c, d)

# unpacking list
a, b, c, d = [10, 20, 30, 'python']
print(a, b, c, d)

t = (1, 2, 3, 4, 5, 6)
a, *b = t
print(a, b)

*a, b = t
print(a, b)

a, b, *c = t
print(a, b, c)

a, *b, c = t
print(a, b, c)