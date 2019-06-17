a = 1
b = a

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]

print(x)
print(y)

y = copy.deepcopy(x)

a = ["hello", "world"]
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

c = copy.deepcopy(a)
print(a is c)
print(a[0] is c[0])