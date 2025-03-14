# Logical operators
# and (and), or (or), not (not)
# and - All conditions must be true.
# If any value is considered false,
# the entire expression will be evaluated as that value.
# The following are considered falsy (as you've seen before):
# 0, 0.0, '', False
# There is also the None type, which is
# used to represent a non-value.

# entry = input('[E]nter [E]xit: ')
# entered_password = input('Password: ')

# allowed_password = '123456'

# if entry == 'E' and entered_password == allowed_password:
#     print('Enter')
# else:
#     print('Exit')

# Short-circuit evaluation
print(True and False and True)
print(True and 0 and True)
