if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    curMax = max(arr)

    newArr = []

    for i in arr:
        if i != curMax:
            newArr.append(i)

    print(max(newArr))