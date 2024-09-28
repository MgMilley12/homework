file = open("17_11481.txt")
lst = [int(x) for x in file]

lst_osob = [x for x in lst if str(abs(x))[0] == '8']
max_osob = max(lst_osob)

ans = []
for i in range(0, len(lst) - 2):
    x, y, z = lst[i], lst[i + 1], lst[i + 2]
    if (str(abs(x))[0] == '6') + (str(abs(y))[0] == '6') + (str(abs(z))[0] == '6'):
        if x + y + z >= max_osob:
            ans.append(x + y + z)
    
print(len(ans), min(ans))
