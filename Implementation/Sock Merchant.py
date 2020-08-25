#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sortedDict = {}

    for i in range(len(ar)):
        if ar[i] not in sortedDict:
            sortedDict[ar[i]] = 1
        else:
            sortedDict[ar[i]] += 1

    finalDict = collections.OrderedDict(sorted(sortedDict.items()))

    pairedSocks = 0

    for key in finalDict:
        pairedSocks += finalDict[key] // 2

    return (pairedSocks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
