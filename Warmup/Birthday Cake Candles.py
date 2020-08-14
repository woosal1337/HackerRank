#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallestCandle = max(ar)
    tallestCandleAmount = 0

    for i in ar:
        if i == tallestCandle:
            tallestCandleAmount += 1

    return tallestCandleAmount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
