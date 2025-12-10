def genTrans():
    money = (10,20,30)
    return money
def sumTrans(trans):
    sum = 0
    for item in trans:
        sum += item
    print("sum of transaction:",sum)
trans = genTrans()
print(genTrans())
sumTrans(trans)
