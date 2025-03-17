# saved_password = '123456'
# entered_password = ''
# repetitions = 0

# while saved_password != entered_password:
#     entered_password = input(f'Your password ({repetitions}x): ')

#     repetitions += 1

# print(repetitions)
# print('The loop above can have infinite repetitions')

text = 'Python'

new_text = ''
for letter in text:
    new_text += f'*{letter}'
    print(letter)
print(new_text + '*')
