mus = []
mus_2 = []
k = 0
f = [int(x) for x in open('17_9704.txt')]
for i in range(len(f) - 1):
    a = len(str(f[i]))
    b = len(str(f[i + 1]))
    if (a == 2 and b != 2) or (a != 2 and b == 2):
        m = int(f[i]) + int(f[i + 1])
        mus.append(m)

for s in range(len(f)):
    if f[s] > max(mus):
        k += 1
        mus_2.append(f[s])
print(k, min(mus_2))