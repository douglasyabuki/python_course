# sys.argv - Running scripts with command-line arguments
# Font = Fira Code (optional comment)
import sys

arguments = sys.argv
arguments_count = len(arguments)

if arguments_count <= 1:
    print('You did not provide any arguments.')
else:
    try:
        print(f'You provided the arguments: {arguments[1:]}')
        print(f'Do something with: {arguments[1]}')
        print(f'Do something else with: {arguments[2]}')
    except IndexError:
        print('Some arguments are missing.')
