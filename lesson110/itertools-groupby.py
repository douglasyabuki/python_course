# groupby - grouping values (itertools)
from itertools import groupby

students = [
    {'name': 'Louis', 'grade': 'A'},
    {'name': 'Leticia', 'grade': 'B'},
    {'name': 'Fabrice', 'grade': 'A'},
    {'name': 'Rosemary', 'grade': 'C'},
    {'name': 'Jane', 'grade': 'D'},
    {'name': 'John', 'grade': 'A'},
    {'name': 'Edward', 'grade': 'B'},
    {'name': 'Andrew', 'grade': 'A'},
    {'name': 'Anderson', 'grade': 'C'},
]


def sort_key(student):
    return student['grade']


grouped_students = sorted(students, key=sort_key)
groups = groupby(grouped_students, key=sort_key)

for key, group in groups:
    print(key)
    for student in group:
        print(student)
