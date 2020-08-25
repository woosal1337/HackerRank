#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    landedApple = 0
    landedOranges = 0

    m = len(apples)  # Amount of apples
    n = len(oranges)  # Amount of oranges

    for i in range(m):
        if s <= apples[i] + a <= t:
            landedApple += 1

    for j in range(n):
        if s <= oranges[j] + b <= t:
            landedOranges += 1

    print(landedApple)
    print(landedOranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
