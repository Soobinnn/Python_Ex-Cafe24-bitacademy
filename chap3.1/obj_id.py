i1 = 10
i2 = 10

print(hex(id(i1)), hex(id(i2)))

l1 = [1,2,3]
l2 = [1,2,3]
print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

print(i1 is i2)
print(l1 is l2)
print(s1 is s2)