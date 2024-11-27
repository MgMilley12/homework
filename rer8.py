#Задача 2 Программирование
from itertools import product

alph = '0123456789ABCDE'

q = 0
for a, b, c, d, e in product(alph, repeat=5):
    if a == '0':
        continue
    num = a + b + c + d + e
    s9 = sum(num.count(x) for x in 'ABCDE')
    if num.count('8') == 1 and s9 > 1:
        q += 1
print(q)
