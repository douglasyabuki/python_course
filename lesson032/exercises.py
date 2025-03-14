"""
Create a program that asks the user to enter an integer number
and informs whether the number is even or odd. If the user does not enter an integer,
inform that it is not an integer number.
"""
# entry = input('Enter a number: ')

# if entry.isdigit():
#     entry_int = int(entry)
#     even_odd = entry_int % 2 == 0
#     even_odd_text = 'odd'

#     if even_odd:
#         even_odd_text = 'even'

#     print(f'The number {entry_int} is {even_odd_text}')
# else:
#     print('You did not enter an integer number')

# try:
#     entry_int = float(entry)
#     even_odd = entry_int % 2 == 0
#     even_odd_text = 'odd'

#     if even_odd:
#         even_odd_text = 'even'

#     print(f'The number {entry_int} is {even_odd_text}')
# except:
#     print('You did not enter an integer number')

"""
Create a program that asks the user for the time and, based on the 
entered time, displays the appropriate greeting. Example:
Good morning 0-11, Good afternoon 12-17, and Good evening 18-23.
"""
# entry = input('Enter the time as an integer: ')

# try:
#     hour = int(entry)

#     if hour >= 0 and hour <= 11:
#         print('Good morning')
#     elif hour >= 12 and hour <= 17:
#         print('Good afternoon')
#     elif hour >= 18 and hour <= 23:
#         print('Good evening')
#     else:
#         print('I do not recognize this time')
# except:
#     print('Please enter only integer numbers')

"""
Create a program that asks for the user's first name. 
If the name has 4 or fewer letters, print "Your name is short"; 
if it has between 5 and 6 letters, print "Your name is normal"; 
if it has more than 6 letters, print "Your name is very long".
"""
name = input('Enter your name: ')
name_length = len(name)

if name_length > 1:
    if name_length <= 4:
        print('Your name is short')
    elif name_length >= 5 and name_length <= 6:
        print('Your name is normal')
    else:
        print('Your name is very long')
else:
    print('Please enter more than one letter.')
