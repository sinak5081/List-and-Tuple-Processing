num = []
while True:
    x = int(input("Enter a number:(0 to finish): "))
    if x == 0:
        break
    else:
        num.append(x)
print("list number before delete negative number")
print(num)
negative = []
for x in num[:]:
    if x < 0:
        negative.append(x)
        num.remove(x)
print("after deleting negative number")
print("list of number:")
print(num)
print("list of negative number is")
print(negative)