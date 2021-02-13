from itertools import product

A = []
B = []

for i in (input().split()):
    A.append(int(i))

for i in (input().split()):
    B.append(int(i))

for i in (list(product(A, B))):
    print(i, end=" ")