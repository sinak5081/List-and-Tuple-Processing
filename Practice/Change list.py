#Assignment operation
x=[1,2,3,4]
print(x)
x[1]=25
print(x)
print("_________________________________________")
#Delete element
print(x)
del x[1]
print(x)
print("_________________________________________")
#Assignment to a slice of the list
y = [2,4,6,8,10]
print(y)
y[:2]=[1,2]
print(y)
print("_________________________________________")
#Joining two lists together
print(x)
print(y)
new_list = x+y
print(new_list)