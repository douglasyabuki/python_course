# The 'random' module generates pseudo-random numbers.
# Note: Pseudo-random means that numbers appear random but are not truly random.
# Therefore, this module shouldn't be used for security or cryptographic purposes.
# Given the same seed and algorithm, the output can become predictable.
# Documentation: https://docs.python.org/3/library/random.html

import random

# Functions:
# seed
#   -> Initializes the random number generator (hence "pseudo-random numbers")
# random.seed(0)

# random.randrange(start, stop, step)
#   -> Generates a random integer within a specific range and step
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(start, stop)
#   -> Generates a random integer within a range (without a step)
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(start, stop)
#   -> Generates a random floating-point number within a given range
r_uniform  = random.uniform(10, 20)
print(r_uniform)