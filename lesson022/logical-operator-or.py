# Logical operators
# and (and), or (or), not (not)
# or - Any true condition makes
# the entire expression evaluate as true.
# If any value is considered true,
# the whole expression will be evaluated as that value.
# The following are considered falsy (as you've seen before):
# 0, 0.0, '', False
# There is also the None type, which is
# used to represent a non-value.

# entry = input('[E]nter [S]exit: ')
# entered_password = input('Password: ')

# allowed_password = '123456'

# if (entry == 'E' or entry == 'e') and entered_password == allowed_password:
#     print('Enter')
# else:
#     print('Exit')

# Short-circuit evaluation
password = input('Password: ') or 'No password'
print(password)
