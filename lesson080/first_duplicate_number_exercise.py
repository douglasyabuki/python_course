"""
Exercise
Create a function that finds the first duplicate number,
considering the second occurrence as the duplication.
Return the duplicated number.

Requirements:
    The order of the duplicated number is considered from the **second**
    occurrence of the number (i.e., the duplicate itself).
    
    Example:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2, and 3 are duplicates (return 3)
        [1, 2, 3, 4, 5, 6] -> Return -1 (no duplicates)
        [1, 4, 9, 8, ->9<-, 4, 8] -> Return 9
        
    If no duplicates are found in the list, return -1.
"""

list_of_integer_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def find_first_duplicate(integer_list):
    checked_numbers = set()
    first_duplicate = -1

    for number in integer_list:
        if number in checked_numbers:
            first_duplicate = number
            break

        checked_numbers.add(number)

    return first_duplicate


for lst in list_of_integer_lists:
    print(
        lst,
        find_first_duplicate(lst)
    )
