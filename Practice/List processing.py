def getGrades(grades):
    for i in range(len(grades)):
        print("Enter ",len(grades[i]),"Average:",end=" ")
        grades[i] = [float(x) for x in input().split()]
def getAve(grades):
    sumGrade = 0
    count = 0
    for i in range(len(grades)):
        count += len(grades[i])
        for j in range(len(grades[i])):
            sumGrade += grades[i][j] * 3
    print("{0:10s} {1:8.2f}".format("Total ave=",sumGrade / (count * 3)))
def Display(grades):
    for i in range(len(grades)):
        for j in range(len(grades[i])):
            print("{0:8.2f}".format(grades[i][j]),end=" ")
term = 3
n1,n2,n3 = 5,3,6
grades = ([0]*term)
grades[0] = ([0] * n1)
grades[1] = ([0] * n2)
grades[2] = ([0] * n3)
getGrades(grades)
getAve(grades)
Display(grades)

