#method append = Add an object to the end of the list
lst1 = [1,2,3]
print(lst1)
lst1.append(4)
print(lst1)
print("____________________________________")
#method count = Counting the number of times an element occurs
lst2 = [1,1,2,3,4,4,4,5,6,7]
print(lst2)
lst2.count(1)
print("count 1 is :",lst2.count(1))
lst2.count(4)
print("count 2 is :",lst2.count(4))
print("____________________________________")
#method index = Searches for a value in a list.
print(lst1)
print("element 2 is:",lst1.index(2))
print(lst2)
print("element 7 is:",lst2.index(7))

#method insert = To insert an element into a list at a desired index
print(lst1)
lst1.insert(2,15)
print(lst1)
print("____________________________________")
#method pop = Removing an element and restoring it
print(lst1)
lst1.pop(0)
print(lst1)
print("____________________________________")
#Delete element
name = ["i am","sina","karimi"]
print(name)
name.remove("i am")
print(name)
print("____________________________________")
#method reserved = This method reverses the elements of the list.
print(lst1)
lst1.reverse()
print(lst1)
print("____________________________________")
#method sort = This method links elements in ascending order.
num = [1,4,52,12,3,2,10,5]
print(num)
num.sort()
print(num)