def F(n):
    if n < 2:
        return n
    if n >= 2:
        return F(n//2) + F(n%2)

k = 0
for n in range(1, 2**30):
    if F(n) == 27:
        k += 1
print(k)