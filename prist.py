# Задача 3 Программирование
for a in range(1000):
    f = 1
    for x in range(1000):
        for y in range(1000):
            if ((x >= 27) or (2 * x < 3 * y) or (a > (x + 2) * (y - 3))) == 0:
                f = 0
                break
        if f == 0:
            break

    if f:
        print(a)
        break
