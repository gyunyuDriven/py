import sys
import os
fd = os.open('set.txt', os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

intro = []
for a in raw_input().split():
    intro.append(int(a))

sups = []
sups.append(intro[1])
i = 0
while i < intro[0]:
    sups.append(0)
    i += 1
while True:
    count = 0
    try:
        x = int(raw_input())
        for i, sup in enumerate(sups):
            if i != x:
                if sup !=0:
                    sups[i] = sup - 1
                    count += 1
        sups[x] += count

    except EOFError as e:
        break
sups[0] = 0
M = max(sups)
for i, s in enumerate(sups):
    if s == M:
        print i
