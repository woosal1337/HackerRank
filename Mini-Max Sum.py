#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxNum = max(arr)
    minNum = min(arr)

    maxSum = sum(arr) - minNum
    minSum = sum(arr) - maxNum

    print(minSum, maxSum)



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
