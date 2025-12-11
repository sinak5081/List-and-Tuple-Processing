money = (10,20,30,40,50,60)
#first method to change
print("before change")
print(money)
print("after change")
money = money[:3] + money[4:]
print(money)
#____________________________________
print("_______________________")
print("second method to change tuple")
print(money)
money = money[:3] + (11,12,13,14) + money[4:]
print(money)
