"""
Iterable -> str, range, etc (__iter__)
Iterator -> an object that can return one value at a time
next -> give me the next value
iter -> give me your iterator
"""
# for letter in text
text = 'Name'  # iterable

# iterator = iter(text)  # iterator

# while True:
#     try:
#         letter = next(iterator)
#         print(letter)
#     except StopIteration:
#         break

for letter in text:
    print(letter)
