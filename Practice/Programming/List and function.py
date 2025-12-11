def getStudent():
    while True:
        a = input("Enter a student name: or Enter (end to finish): ")
        if a.strip().lower() == "end":
            break
        else:
            b = float(input("Enter student grade: "))
            c = int(input("Enter student id:"))
        name.append(a)
        grade.append(b)
        id.append(c)
    return name , grade,id
def display(name,grade,id):
    for name,grade,id in zip(name,grade,id):
        print("name:",name,"average:",grade,"id:",id)
def minAvg(name , grade):
    if not grade:
        print("No student Entered")
        return
    min_grade = min(grade)
    idx = grade.index(min_grade)
    print("min grade is:",min_grade , "by student: ",name[idx])
def maxAvg(name,grade):
    max_grade = max(grade)
    idx = grade.index(max_grade)
    print("max grade is:",max_grade,"by student: ",name[idx])
def remove_student(name,grade , id):
    target = int(input("Enter student id for delete:"))
    index = id.index(target)
    del name[index]
    del grade[index]
    del id[index]
    print("delete successful")
def menu():
    print("1.Enter value")
    print("2.show list of value")
    print("3.find min average")
    print("4.find max average:")
    print("5.delete student")
    print("6.Exit")
    choice = int(input("Enter your select(1-6): "))
    return choice
name = []
grade = []
id = []
while True:
    c = menu()
    if c == 1:
        getStudent()
    elif c == 2:
        display(name,grade,id)
    elif c == 3:
        minAvg(name,grade)
    elif c == 4:
        maxAvg(name,grade)
    elif c == 5:
        remove_student(name,grade,id)
    else:
        break
