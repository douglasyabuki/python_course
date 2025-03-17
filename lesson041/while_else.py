""" while/else """
string = 'Any value'

i = 0
while i < len(string):
    letter = string[i]

    if letter == ' ':
        break

    print(letter)
    i += 1
else:
    print('Did not find a space in the string.')

print('Outside the while loop.')
