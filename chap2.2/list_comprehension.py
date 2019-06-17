results = []
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = i * i
    results.append(result)
print(results)

results = [result*result for result in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(results)

