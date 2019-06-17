t = (1, 2, 3)
print(t, type(t))

t = 1, 2, 'python'
print(t, type(t))

print(t[-2], t[-1], t[0], t[1], t[2])
print(t[1:3])
print(t[:])

print(t*2)
print(t + (3,4,5))
print(len(t))
print(5 in t)

s = set(t)
print(s, type(s))

l = list(s)
print(l, type(l))

t = tuple(l)
print(t, type(t))
