phrase = 'aaaooo'

i = 0
most_frequent_count = 0
most_frequent_letter = ''

while i < len(phrase):
    current_letter = phrase[i]

    if current_letter == ' ':
        i += 1
        continue

    current_letter_count = phrase.count(current_letter)

    if most_frequent_count < current_letter_count:
        most_frequent_count = current_letter_count
        most_frequent_letter = current_letter

    i += 1

print(
    'The letter that appeared the most was '
    f'"{most_frequent_letter}" which appeared '
    f'{most_frequent_count} times'
)
