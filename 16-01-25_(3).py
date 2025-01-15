from fnmatch import fnmatch
n = 5401037
n += 18579 - n % 18579

for i in range(n, 10**10, 18579):
    if fnmatch(str(i), '54?1?3*7'):
        print(i, i // 18579)
        