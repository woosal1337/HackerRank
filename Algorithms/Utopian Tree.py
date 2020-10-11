#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    theLength = 0  # Representing 0's day

    if n == 0:
        return 1

    x = 0
    if n > 0:
        while x != n+1:
            if x % 2 == 0:
                theLength += 1
            else:
                if x % 2 != 0:
                    theLength *= 2
            x += 1

    return theLength
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
