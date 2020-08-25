#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    newList = bill.copy()
    newList.pop(k)
    theSum = 0

    for i in range(len(newList)):
        theSum += newList[i]

    if (theSum / 2) == b:
        print("Bon Appetit")
    else:
        print(b - (theSum / 2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
