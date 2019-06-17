a = {1, 2, 3}
print(a, type(a))

print(len(a))
print(2 in a)
print(2 not in a)

# s.add(4)
# s.add(1)
# s.discard(2)
# s.remove(3)
# s.update({2,3})
# s.clear()

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s4 = s1.difference(s2)
print(s4)

s5 = s1.symmetric_difference(s2)
print(s5)

print(s1.issuperset(s4))
print(s5.issuperset(s1))
print(s2.issuperset(s3))