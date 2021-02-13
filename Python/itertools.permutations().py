import itertools

currentInput = input().split()
inputName = currentInput[0]
inputInt = int(currentInput[1])

theFirstInp = list(itertools.permutations(inputName, inputInt))

finalList = []

for i in range(len(theFirstInp)):
    finalList.append([])
    for j in theFirstInp[i]:
        finalList[i] += j
finalList.sort()

for i in finalList:
    currentStr = ""
    for j in i:
        currentStr += j
    print(currentStr)



