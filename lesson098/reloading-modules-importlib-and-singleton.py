import importlib

import module98

print(module98.variable)

for i in range(10):
    importlib.reload(module98)
    print(i)

print('Fim')