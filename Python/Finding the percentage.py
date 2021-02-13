if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    totalScores = 0
    for i in student_marks[query_name]:
        totalScores += i


    finalAvg = ("%.2f" % round((totalScores / len(student_marks[query_name])), 2))

    if str(finalAvg)[-2] == ".":
        print(f"{finalAvg}0")
    else:
        print(finalAvg)


