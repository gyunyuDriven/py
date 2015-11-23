def paycalc(storeCoin, pay):
    payEach = [int(x) for x in pay.split()]
    price = payEach[0]
    payment = payEach[1] * 500 + payEach[2] * 100 + payEach[3] * 50 + payEach[4] * 10
    temp = storeCoin
    for (i, x) in enumerate(payEach[1:4]):
        storeCoin[i] += x
    hundred = int((payment - price) /100)
    # 百円の数
    fifty = int(((payment - price) - hundred * 100)/50)
    # 50円の数
    ten = int(((payment - price) - hundred * 100)/10)
    # 10円の数
    oturiNet = [0,0,0,0]
    if storeCoin[1] - hundred >= 0:
        oturiNet[1] =  hundred
    else:
        print("impossible")
        storeCoin = temp
        return
    if storeCoin[2] - fifty >= 0:
        oturiNet[2] = fifty
    if storeCoin[3] - int(ten - oturiNet[2] * 5) >= 0:
        oturiNet[3] =int(ten - oturiNet[2] * 5)
    else:
        print("impossible")
        storeCoin = temp
        return
    o = int(oturiNet[0] * 500 + oturiNet[1] * 100 + oturiNet[2] * 50 + oturiNet[3] * 10)
    if payment - price != o:
        print("impossible")
        storeCoin = temp
        return
    else:
        print("{} {} {} {}".format(oturiNet[0],oturiNet[1],oturiNet[2],oturiNet[3]))
        hiki = []
        for a,b in zip(storeCoin,oturiNet):
            hiki.append(int(a-b))
        for (i, x) in enumerate(hiki):
            storeCoin[i] = int(x)

import sys
import os
fd = os.open('set.txt', os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

storeCoin = [int(x) for x in input().split()]

lineNum = int(input())
payAll =[]
for i in range(lineNum):
    payAll.append(input())

for paya in payAll:
    paycalc(storeCoin,paya)
