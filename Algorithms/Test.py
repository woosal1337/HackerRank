import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    upperCaseChar = 0
    lowerCaseChar = 0
    numbersTotal = 0
    specialChar = 0

    passLen = len(password)

    for i in range(len(lower_case)):
        if lower_case[i] in password:
            lowerCaseChar += 1
        if upper_case[i] in password:
            upperCaseChar += 1

    for i in range(len(numbers)):
        if numbers[i] in password:
            numbersTotal += 1

    for i in range(len(upper_case)):
        if upper_case[i] in password:
            upperCaseChar += 1

    for i in range(len(special_characters)):
        if special_characters[i] in password:
            specialChar += 1

    print(upperCaseChar, lowerCaseChar, numbersTotal, specialChar)

    totalNeeded = 0

    if upperCaseChar == 0:
        totalNeeded += 1
    if lowerCaseChar == 0:
        totalNeeded += 1
    if numbersTotal == 0:
        totalNeeded += 1
    if specialChar == 0:
        totalNeeded += 1



    if totalNeeded > 6 - passLen:
        return totalNeeded
    else:
        return (6 - passLen)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
