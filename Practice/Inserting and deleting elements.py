list = [[11,12,5],[1,2,3],[6,20,1],[12,1,1]]
print("before delete:")
print(list)
#Removing values ​​from a two-dimensional list
#del list[row]
print("after delete:")
del list[1]
print(list)
print("________________________________")
#________________________
#Insert values
#list.insert
print("before insert:")
print(list)
print("after insert:")
list.insert(1,[100,101,102])
print(list)