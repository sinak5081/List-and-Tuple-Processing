def getTemp(temp):
    for i in range(len(temp)):
        temp[i] = [int(x) for x in input("Enter five values:").split()]
def Display(temp):
    print("Contents of list:")
    print("  ",end=" ")
    for h in hours:
        print("{0:4s}".format(h),end="  ")
    print()
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            print("{0:5d}".format(temp[i][j]),end=" ")
        print()
    print("___________________________")
def findMean(temp):
    days = ["wed","thur","friday"]
    print("{0:7s} {1:7s}".format("Days","Average"))
    print("___________________________")
    for i in range(len(temp)):
        daysum = 0
        for j in range(len(temp[0])):
            daysum += temp[i][j]
        print("{0:7s} {1:8.2f}".format(days[i],
            daysum /len(temp[0])))
hours = ["8am","10am","12pm","2pm","4pm"]
rows = 3
cols = 5
temp = [ ([0] * cols) for row in range(rows)]
getTemp(temp)
Display(temp)
findMean(temp)
#The five values ​​you enter three times are the temperatures at different times over three days.
#Hours = 20 , 16,12,10,8
#days = wed , thurs , friday
