# Deque - Working with LIFO and FIFO
# deque - Double-ended queue
#
# LIFO and FIFO
# Stack and Queue

# LIFO (Last In First Out)
# Stack
# Means that the last item inserted is the first one removed (list)
# Article (in Portuguese):
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
# Video (in Portuguese):
# https://youtu.be/svWVHEihyNI
# Removing items from the end: O(1) Constant time
# Removing items from the beginning: O(n) Linear time

from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅ Good (LIFO with list)
# Initial list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(10)  # Add to the end
# Now: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.append(11)  # Add to the end
# Now: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ultimo_removido = lista.pop()  # Remove from the end
# After removal: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Last removed:', ultimo_removido)
print('List:', lista)
print()


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🚫 Bad (FIFO with list)
# Initial list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 10)  # Insert at beginning
# Now: [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 11)  # Insert at beginning
# Now: [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro_removido = lista.pop(0)  # Remove from beginning (inefficient)
# After removal: [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('First removed:', primeiro_removido)
print('List:', lista)
print()

# FIFO (First In First Out)
# Queue
# Means that the first item inserted is the first one removed (deque)
# Article (in Portuguese):
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Video (in Portuguese):
# https://youtu.be/RHb-8hXs3HE
# Removing items from the end: O(1) Constant time
# Removing items from the beginning: O(1) Constant time

# ✅ Good (FIFO with deque)

correct_queue: deque[int] = deque()
correct_queue.append(3)       # Add at the end
correct_queue.append(4)       # Add at the end
correct_queue.append(5)       # Add at the end
correct_queue.appendleft(2)   # Add at the beginning
correct_queue.appendleft(1)   # Add at the beginning
correct_queue.appendleft(0)   # Add at the beginning
print(correct_queue)          # deque([0, 1, 2, 3, 4, 5])
correct_queue.pop()           # Removes 5 (end)
correct_queue.popleft()       # Removes 0 (beginning)
print(correct_queue)          # deque([1, 2, 3, 4])
