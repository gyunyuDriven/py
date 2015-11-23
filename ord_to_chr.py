from __future__ import print_function

def search_ast2(b1,x,y,w,h):
    count = 0
    tps =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for tp in tps:
        if b1[((y+tp[0])+h)%h][((x+tp[1])+w)%w] == "*":
            count += 1
    return count

def search_ast(a1,b1,x,y,w,h):
    count = search_ast2(b1,x,y,w,h)
    if a1[y][x] == "*":
        if count == 2 or count == 3:
            pass
        else:
            a1[y][x] = "."
    else:
        if count == 3:
            a1[y][x] = "*"


def print_format(a1,w,h):
    i = 0
    j = 0
    while i < h:
        while j < w:
            print(a1[i][j],end = "")
            j += 1
        print("")
        j = 0
        i += 1

import sys
import os
fd = os.open('set.txt', os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

gen  = int(raw_input())
h = int(raw_input())
w = int(raw_input())
a1 = []
while True:
    try:
        a = [a for a in raw_input()]
        a1.append(a)
    except EOFError:
        break
import copy
b1 = copy.deepcopy(a1)
i = 0
j = 0
while gen > 0:
    i = 0
    b1 = copy.deepcopy(a1)
    while i < h:
        j = 0
        while j < w:
            search_ast(a1,b1,j,i,w,h)
            j += 1
        i += 1
    gen -=1
i = 0
j = 0

while i < h:
    while j < w:
        print(a1[i][j],end = "")
        j += 1
    print("")
    j = 0
    i += 1
