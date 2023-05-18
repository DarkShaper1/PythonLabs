from random import randint
arr = []
with open('TSLA.csv') as f:
    next(f)
    for line in f:
        data = line.replace('\n', '').split(',')
        arr.append(data[5])
money = 100
for i in range(len(arr) - 1):
    if arr[i] < arr[i+1]:
        money = money * (float(arr[i+1]) / float(arr[i]))
print(money)
money = 100
for i in range(len(arr) - 1):
    if randint(0, 1) == 1:
        money = money * (float(arr[i+1]) / float(arr[i]))
print(money)
