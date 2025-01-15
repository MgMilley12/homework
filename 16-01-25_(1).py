from itertools import product

k = 0
for i, t in enumerate(product('АВНРЬЯ', repeat=5), 1):
    s = ''.join(t)
    if s[0] != 'Я' and s.count('Ь') < 2 and 'ЯЯ' not in s:
        k = i
print(k)
