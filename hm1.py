#Задача 1 Программирование
def conv(n):
    d = ''
    while n:
        d = str(n % 3) + d
        n //= 3
    return d


def R(N):
    tr = conv(N)
    if N % 2 == 0:
        t = '2' + tr + conv(int(tr[-1]) * 2)
    else:
        t = conv(int(tr[0]) * 2) + tr + '2'
    return int(t, 3)


a = [R(N) for N in range(1, 100) if R(N) > 100]

print(min(a))
