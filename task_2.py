f = open('24-228_5644.txt').readline()
s = ''
l = -1
for i in range(len(f) - 1):
    if f[i] == 'X' and f[i + 1] == 'X':
        if l != -1:
            f1 = f[l + 2:i]
            if len(f1) == 11 and f1.isdigit():
                if f1[0] == '3' and f1[5:7] == '78' and f1[9:] == '45':
                    s = max(s, f1)
        l = i
n = 0
ns = 1
for z in s:
    if int(z) % 2 == 1:
        n += int(z)
    else:
        ns *= int(z)
print(ns + n)
