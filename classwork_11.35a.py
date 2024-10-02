import random
l = 10
m = [random.randint(-100, 100) for i in range(l)]
print("Нач. мас. ", m)
a = m[1]
b = m[2]
for s in range(len(m)):
    if m[s] < 0:
        m[s] = m[s] + a
    else:
        m[s] = m[s] + b
print("Кон. мас. ", m)

#11.35b

l = 10
m = [random.randint(-100, 100) for i in range(l)]
print("Нач. мас. ", m)
for s in range(len(m)):
    if m[s] % 2 == 0:
        m[s] = m[s] * 2
    else:
        m[s] = m[s] - 1
print("Кон. мас. ", m)