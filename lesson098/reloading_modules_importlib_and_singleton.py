import importlib

import lesson098.module098 as module098

print(module098.variable)

for i in range(10):
    importlib.reload(module098)
    print(i)

print('Fim')