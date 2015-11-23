def rot13(ch):
    ascii = ord(ch)
    if ascii  >= 65 and ascii < 97:
        return chr(((ascii - 65 + 13) % 26) +65)
    if ascii >=  97 and ascii < 123:
        return chr(((ascii - 97 + 13) % 26) +97)
    else:
        return ch

import sys
import os
fd = os.open('set.txt', os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

passage = raw_input()
chs =[c for c in passage]
rot13passage =""
for ch in chs:
    rot13passage += rot13(ch)
print(rot13passage)
