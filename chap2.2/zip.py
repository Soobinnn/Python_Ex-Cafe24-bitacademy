seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))

for t in z:
    print(t, type(t))

t1 = [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
seq1, seq2 = zip(*t1)
print(seq1)
print(seq2)
