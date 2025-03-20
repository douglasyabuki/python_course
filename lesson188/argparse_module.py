# argparse.ArgumentParser for more complex command-line arguments
# Official Tutorial:
# https://docs.python.org/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Displays "Hello World" on the screen',
    # type=str,  # Argument type
    metavar='STRING',
    # default='Hello World',  # Default value
    required=False,
    action='append',  # Accepts argument multiple times
    # nargs='+',  # Accepts multiple values per occurrence
)

parser.add_argument(
    '-v', '--verbose',
    help='Displays logs',
    action='store_true'
)

args = parser.parse_args()

if args.basic is None:
    print('You did not provide a value for -b.')
    print(args.basic)
else:
    print('The value(s) for basic:', args.basic)

print('Verbose mode:', args.verbose)
