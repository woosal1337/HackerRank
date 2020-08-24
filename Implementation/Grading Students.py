import math

grades = [73, 67, 38, 33]

def gradingStudents(grades):
    for i in range(len(grades)):
        if 0 <= grades[i] <= 100:
            if grades[i] % 5 != 0:
                nextFive = math.ceil(grades[i] / 5) * 5
                if grades[i] < 38:
                    print(grades[i])
                elif nextFive - grades[i] < 3:
                    grades[i] += nextFive - grades[i]
                    return (grades[i])
                else:
                    return (grades[i])

gradingStudents(grades)