import random
l = 10
m = [random.randint(-100, 100) for i in range(l)]
n = random.randint(-100, 100)
print("Число N - ", n, "\nНач. мас. ", m)
k = m[1]
for s in range(len(m)):
    if m[s] > 0 and m[s] != 0:
        m[s] = m[s] - k
    elif m[s] < 0:
        m[s] = m[s] - n
print("Кон. мас. ", m)

#11.36b

l = 10
m = [random.randint(-100, 100) for i in range(l)]
n = random.randint(-100, 100)
a = random.randint(-100, 100)
b = random.randint(-100, 100)
print("Число N - ", n,"\nЧисло A - ", a,"\nЧисло B - ", b, "\nНач. мас. ", m)
k = m[1]
for s in range(len(m)):
    if m[s] > 0:
        m[s] = m[s] - a
    elif m[s] < 0:
        m[s] = m[s] + b
    elif m[s] == 0:
        m[s] = m[s] + n
print("Кон. мас. ", m)