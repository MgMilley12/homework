m_1 = []
m_2 = []
c = 0
f = [int(x) for x in open('17_9704.txt')]
for i in range(len(f) - 1):
    a = len(str(f[i]))
    b = len(str(f[i + 1]))
    if (a == 2 and b != 2) or (a != 2 and b == 2):
        m = int(f[i]) + int(f[i + 1])
        m_1.append(m)

for s in range(len(f)):
    if f[s] > max(m_1):
        c += 1
        m_2.append(f[s])
print(c, min(m_2))
