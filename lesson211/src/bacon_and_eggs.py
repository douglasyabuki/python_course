"""
1 - Receive an integer number
2 - If the number is a multiple of 3 and 5:
    Bacon and eggs
3 - If the number is NOT a multiple of 3 and 5:
    Go hungry
4 - If the number is a multiple of 3 only:
    Bacon
5 - If the number is a multiple of 5 only:
    Eggs
"""


def bacon_and_eggs(n):
    assert isinstance(n, int), 'n must be int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon and eggs'

    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Eggs'

    return 'Go hungry'
