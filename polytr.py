#Задача 4 Программирование
def f(n, trg):
    if n == trg:
        return 1
    elif n < trg or n == 27:
        return 0
    else:
        return f(n - 1, trg) + f(n - 5, trg)


print(f(32, 26) * f(26, 24) * f(24, 17))
