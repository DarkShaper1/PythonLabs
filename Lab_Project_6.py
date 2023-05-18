import numpy as np

# Задача 1
a = np.arange(1, 16).reshape(3, 5)
a = np.transpose(a)
print(a)

print()
# Задача 2
a = np.arange(25).reshape(5, 5)
a = np.transpose(a)
for i in a:
    b = np.array(i)
    print(b)

print()
# Задача 3
array = np.random.uniform(0, 1, [10, 3])
b = np.zeros((10, 3))
print(array)
print()
for i in range(10):
    for g in range(3):
        b[i, g] = abs(array[i, g]-0.5)
idk = np.argsort(b)
for i in range(10):
    ind = idk[i][0]
    print(f'Близкое число к 0.5 в {i+1} строке {array[i][ind]}')


