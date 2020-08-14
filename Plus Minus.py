#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    negSum = 0
    posSum = 0
    zeroSum = 0
    listLen = len(arr)

    for i in arr:
        if i < 0:
            negSum += 1
        else:
            if i > 0:
                posSum += 1
            else:
                if i == 0:
                    zeroSum += 1

    print("%.6f" % (posSum / listLen))
    print("%.6f" % (negSum / listLen))
    print("%.6f" % (zeroSum / listLen))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
