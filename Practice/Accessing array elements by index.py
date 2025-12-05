num = [5,10,15,20,25,30,35]
#The following command accesses the following element:
x = num[0]
print(x)
print("___________________________________")
x = num[5]
print(x)
print("___________________________________")
x = num[-2]
print(x)
print("___________________________________")
# Using loops and the in operator
for item in num:
    print(item,end = " ")

print("___________________________________")
#Cut part of the list
#_________________________________________
print("x=",num)
print("x[:2]:",num[:2])
print("x[:4]:",num[:4])
y = num[3:6]
print("y is:",y)