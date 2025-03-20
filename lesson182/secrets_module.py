# The 'secrets' module generates cryptographically secure random numbers.
import secrets

# import string as s
# from secrets import SystemRandom as Sr

# Example of generating a secure random string (uncomment to use):
# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))  # noqa: E501
# One-liner command example:
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"  # noqa: E501

# Using SystemRandom to generate cryptographically secure numbers
random = secrets.SystemRandom()

# Example usages (uncomment to use):
# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

# Functions:
# seed
#   -> DOES NOTHING (has no effect)
random.seed(10)

# random.randrange(start, stop, step)
#   -> Generates a random integer within a specific range and step
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(start, stop)
#   -> Generates a random integer within a range (no step)
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(start, stop)
#   -> Generates a random floating-point number within a given range
r_uniform = random.uniform(10, 20)
print(r_uniform)

# random.shuffle(mutable_sequence) -> Shuffles the original list
names = ['John', 'Doe', 'Joe', 'Tho']
# random.shuffle(names)  # Uncomment to shuffle securely
print(names)

# random.sample(iterable, k=N)
#   -> Selects elements from the iterable without repeating values
new_names = random.sample(names, k=3)
print(names)
print(new_names)

# random.choices(iterable, k=N)
#   -> Selects elements from the iterable allowing repeated values
new_names = random.choices(names, k=3)
print(names)
print(new_names)

# random.choice(iterable) -> Selects a single random element
print(random.choice(names))
