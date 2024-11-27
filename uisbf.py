#Задача 5 Введение в ИТ
def sg(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False


m = 10 ** 10
for a in range(0, 100):
    for b in range(a, 100):
        c = 0
        for i in range(2, 200):
            x = i / 2
            if not (sg(15, 40, x)) or (not (sg(21, 63, x) and not (sg(a, b, x))) or not (sg(15, 40, x))):
                c = c + 1

        if c == 198:
            m = min(m, b - a)

print(m)
