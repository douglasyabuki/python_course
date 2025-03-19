# Implementing the Iterator protocol in Python
# This is just a lesson to introduce the collections.abc protocols in
# Python. Any other protocol can be implemented by following the same
# structure used in this lesson.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    my_list = MyList()
    my_list.append('John', 'Doe')
    my_list[0] = 'Joe'
    my_list.append('Tho')
    # print(my_list[0])
    # print(len(my_list))
    for item in my_list:
        print(item)
    print('---')
    for item in my_list:
        print(item)
    print('---')
