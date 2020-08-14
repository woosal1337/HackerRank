#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alicePoints = 0
    bobPoints = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            alicePoints += 1
        else:
            if a[i] < b[i]:
                bobPoints += 1
                
    return alicePoints,bobPoints

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
