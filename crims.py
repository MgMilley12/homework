#Задача 5 Программирование
from fnmatch import fnmatch

count = 0
for x in range(1203450670890, 10 ** 13):
    if fnmatch(str(x), '12?345?67089?') and x % 206 == 0:
        count += 1
        print(x, x // 206)
        if count > 4:
            break
