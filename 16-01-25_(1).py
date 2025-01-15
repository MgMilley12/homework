def f(n, t):
    if n < t or n == 24:
        return 0
    if n == t:
        return 1
    return f(n - 1, t) + f(n - 6, t) + f(n // 2, t)


print(f(34, 20) * f(20, 19) * f(19, 6))
