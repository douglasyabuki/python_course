# count is an endless iterator (itertools)
from itertools import count

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)

print('c1 has __iter__?', hasattr(c1, '__iter__'))
print('c1 has __next__?', hasattr(c1, '__next__'))
print('r1 has __iter__?', hasattr(r1, '__iter__'))
print('r1 has __next__?', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()
print('range')
for i in r1:
    print(i)
