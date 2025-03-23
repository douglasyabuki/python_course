import re

# Regular expression to check if the input is a digit or a dot
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    """Checks if the input string is a number or a dot."""
    return bool(NUM_OR_DOT_REGEX.search(string))


def convertToNumber(string: str):
    """Converts a string to a float or int, depending on whether it has decimal places."""
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


def isValidNumber(string: str):
    """Validates if the string can be converted to a float."""
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str):
    """Checks if the string is empty."""
    return len(string) == 0
