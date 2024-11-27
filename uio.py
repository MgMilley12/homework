#Задача 3 Введение в ИТ
from itertools import product

alph = 'АИКМНОПЯ'
q = 0

for idx, p in enumerate(product(alph, repeat=6)):
    if idx % 2 == 0 and p[0] != 'М' and p.count('И') == 3:
        q += 1

print(q)
