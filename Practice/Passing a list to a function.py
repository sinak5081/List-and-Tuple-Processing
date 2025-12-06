def enter(lst):
    while True:
        num = int(input("Enter a number:"))
        if num != 0:
            lst.append(num)
        else:
            break
def negfunc(lst):
    print("negative are: ")
    neg = 0
    for item in lst:
        if item < 0:
            print(item,end=" ")
            neg += 1
    print("number of negative is",neg)
def posfunc(lst):
    print("positive number is:")
    pos = 0
    for item in lst:
        if item > 0:
            print(item,end=" ")
            pos += 1
    print("positive number is:",pos)
def find(lst):
    x = int(input("Enter your number to find:"))
    if x in lst:
        print("your number in list")
    else:
        print("your number not in list")
list = []
enter(list)
print(list)
negfunc(list)
posfunc(list)
find(list)