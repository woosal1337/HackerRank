#!/bin/python3
import operator
import math
import os
import random
import re
import sys
import collections

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    sortedDict = {}

    for i in range(len(arr)):
        if arr[i] not in sortedDict:
            sortedDict[arr[i]] = 1
        else:
            sortedDict[arr[i]] += 1

    finalDict = collections.OrderedDict(sorted(sortedDict.items()))

    highest = max(finalDict.items(), key=operator.itemgetter(1))[0]
    return (highest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
