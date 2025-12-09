#1.Indexing
x = (12,22,33)
#Index one
print(x[0])
#Index two
print(x[1])
#show you class tuple
print(type(x))
print("______________________")
#Accessing a slice of a tuple
t = (10,20,30,40,50,60)
#Second index to last index
print(t[2:])
print("_________________")
#Indexes one to three
print(t[:3])
print("_________________")
#Third index to last index
print(t[3:6])
print("_______________________________________")
#Finding the largest and smallest tuple value
#min:Smallest tuple value
print(min(t))
#max:Largest tuple value
print(max(t))
print("__________________________________")
#Joining two tuples
print("before joining two tuple:")
print(x)
print(t)
print("after joining two tuple:")
c = x+t
print(c)
print(type(c))
print("________________________________________")
#________________________________
#Accessing tuple elements with a for loop
#first method
print("first method:")
for item in t:
    print(item,end="    ")
print()
print("second method:")
#second method
for i in range(len(t)):
    print(t[i],end="    ")
print()
print("______________________________________________")
#__________________________________
#Tuple repetition
t = (5,) * 3
print(t)
t = (1,2,3) * 2
print(t)
print("______________________________________________")
#Sorting and converting tuples to lists
tup = (20,10,30,5,60,40,50)
print(type(tup))
tup1 = sorted(tup)
print(tup1)
print(type(tup1))
print("____________________________________________")
#Counting the number of repetitions
t1 = (1,20,5,23,5,1,1)
print(t1.count(1))
print(t1.count(5))
