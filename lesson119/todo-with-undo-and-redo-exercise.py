# Exercise - To-do list with undo and redo
# Coding music suggestion: Everybody Wants to Rule the World - Tears for Fears
# todo = [] -> empty task list
# todo = ['make coffee'] -> Add "make coffee"
# todo = ['make coffee', 'go for a walk'] -> Add "go for a walk"
# undo = ['make coffee',] -> redo ['go for a walk']
# undo = [] -> redo ['go for a walk', 'make coffee']
# redo = todo ['make coffee']
# redo = todo ['make coffee', 'go for a walk']

import json
import os


def list_tasks(tasks):
    print()
    if not tasks:
        print('No tasks to show')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')
    print()


def undo(tasks, redo_tasks):
    print()
    if not tasks:
        print('No tasks to undo')
        return

    task = tasks.pop()
    print(f'{task=} removed from task list.')
    redo_tasks.append(task)
    print()
    list_tasks(tasks)


def redo(tasks, redo_tasks):
    print()
    if not redo_tasks:
        print('No tasks to redo')
        return

    task = redo_tasks.pop()
    print(f'{task=} added back to task list.')
    tasks.append(task)
    print()
    list_tasks(tasks)


def add(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('You did not type a task.')
        return
    print(f'{task=} added to task list.')
    tasks.append(task)
    print()
    list_tasks(tasks)


def read_file(tasks, file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('File does not exist')
        save(tasks, file_path)
    return data


def save(tasks, file_path):
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


FILE_PATH = 'lesson119/lesson119.json'
tasks = read_file([], FILE_PATH)
redo_tasks = []

while True:
    print('Commands: list, undo, redo')
    task = input('Type a task or command: ')

    commands = {
        'list': lambda: list_tasks(tasks),
        'undo': lambda: undo(tasks, redo_tasks),
        'redo': lambda: redo(tasks, redo_tasks),
        'clear': lambda: os.system('clear' if os.name != 'nt' else 'cls'),
        'add': lambda: add(task, tasks),
    }

    command = commands.get(task) if commands.get(task) is not None else commands['add']
    command()
    save(tasks, FILE_PATH)
