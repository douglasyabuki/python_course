# Example of set
letters = set()  # Create an empty set

while True:
    letter = input('Enter a letter: ')
    letters.add(letter.lower())  # Add the letter to the set (convert to lowercase)

    if 'l' in letters:  # Check if 'l' is in the set
        print('CONGRATULATIONS!')
        break  # Stop the loop when 'l' is found

    print(letters)  # Print the set contents
