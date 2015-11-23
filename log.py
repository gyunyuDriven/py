import sys
import os
fd = os.open('set.txt', os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

a = [0,1,2,3]
for aa in a:
    if aa == 0:
        aa = 100
        print aa
print[a]
