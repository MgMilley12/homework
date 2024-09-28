from fnmatch import *

for z in range(98591, 10**12 + 1, 98591):
    if fnmatch(str(z), '12?3*456??9'):
        print(z, z // 98591)

