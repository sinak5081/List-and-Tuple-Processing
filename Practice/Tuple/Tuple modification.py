#First method
t = (10,20,30,40)
t = t[:2] + t[3:]
print(t)
#second method
t = (5,10,15,20,30)
t = t[:2] + (2,4,6) + t[2:]
print(t)