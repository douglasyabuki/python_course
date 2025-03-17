# Yield from (Delegating Generators)

def gen1():
    print('STARTED GEN1')
    yield 1
    yield 2
    yield 3
    print('FINISHED GEN1')


def gen3():
    print('STARTED GEN3')
    yield 10
    yield 20
    yield 30
    print('FINISHED GEN3')


def gen2(gen=None):
    print('STARTED GEN2')
    if gen is not None:
        yield from gen  # Delegates execution to the passed generator
    yield 4
    yield 5
    yield 6
    print('FINISHED GEN2')


# Creating generators
g1 = gen2(gen1())  # Passes gen1() to gen2()
g2 = gen2(gen3())  # Passes gen3() to gen2()
g3 = gen2()        # Calls gen2() without an argument

# Iterating through the generators
for number in g1:
    print(number)
print()

for number in g2:
    print(number)
print()

for number in g3:
    print(number)
print()
