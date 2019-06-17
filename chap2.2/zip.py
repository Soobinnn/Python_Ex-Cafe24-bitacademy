seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))

for idx, (a,b) in enumerate(z):
    print('%d: %s, %s'%(idx, a,b))


for t in z:
    print(t, type(t))

# 짝지어진 순차 자료형을 다시 풀어내는 예제
t1 = [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
seq1, seq2 = zip(*t1)
print(seq1)
print(seq2)

