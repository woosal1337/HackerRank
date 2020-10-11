#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    totalBeaDays = 0

    # |a-reversedA| / k % 2 == 0 ""
    for z in range(i, j + 1):
        strZ = str(z)
        reversedZ = strZ[::-1]

        while reversedZ[0] == "0":
            reversedZ = reversedZ[1:]

        theDiff = abs(int(z) - int(reversedZ))
        if theDiff % k == 0:
            totalBeaDays += 1

    return totalBeaDays


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
