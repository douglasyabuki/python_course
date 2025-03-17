"""
Create a shopping list using lists.
The user should be able to:
- Insert items
- Delete items
- List items

Ensure the program does not crash due to non-existent indices.
"""
import os

shopping_list = []

while True:
    print('Select an option')
    option = input('[i]nsert [d]elete [l]ist: ')

    if option == 'i':
        # os.system('clear')  # Use 'cls' on Windows
        os.system('cls')
        value = input('Item: ')
        shopping_list.append(value)
    elif option == 'd':
        index_str = input('Enter the index to delete: ')

        try:
            index = int(index_str)
            del shopping_list[index]
        except ValueError:
            print('Please enter an integer.')
        except IndexError:
            print('Index does not exist in the list.')
        except Exception:
            print('Unknown error.')
    elif option == 'l':
        # os.system('clear')  # Use 'cls' on Windows
        os.system('cls')

        if len(shopping_list) == 0:
            print('Nothing to list.')

        for i, value in enumerate(shopping_list):
            print(i, value)
    else:
        print('Please choose i, d, or l.')
