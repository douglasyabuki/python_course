# Operators "in" and "not in"
# Strings are iterable
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# name = 'Otávio'
# print(name[2])
# print(name[-4])
# print('vio' in name)
# print('zero' in name)
# print(10 * '-')
# print('vio' not in name)
# print('zero' not in name)

name = input('Enter your name: ')
search = input('Enter what you want to find: ')

if search in name:
    print(f'{search} is in {name}')
else:
    print(f'{search} is not in {name}')
