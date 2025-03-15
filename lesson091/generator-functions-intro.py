# Introduction to Generator Functions in Python

# generator expression (alternative)
# generator = (n for n in range(1_000_000))

def generator(n=0, maximum=10):
    """A generator function that yields numbers from n up to maximum."""
    while True:
        yield n  # Yields the current value of n
        n += 1

        if n >= maximum:
            return  # Stops the generator when n reaches the limit


gen = generator(maximum=1_000_000)

# Iterating over the generator
for n in gen:
    print(n)
