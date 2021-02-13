if __name__ == '__main__':
    studentList = []
    studentNames = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentList.append([name, score])

    studentList.sort(key=lambda studentList: studentList[1])
    currentLow = studentList[0][1]
    secondCurrentLow = currentLow

    for i in range(len(studentList)):
        if studentList[i][1] != currentLow:
            secondCurrentLow = studentList[i][1]
            break

    for i in range(len(studentList)):
        if studentList[i][1] == secondCurrentLow:
           studentNames.append(studentList[i][0])

    studentNames.sort()

    for i in studentNames:
        print(i)


