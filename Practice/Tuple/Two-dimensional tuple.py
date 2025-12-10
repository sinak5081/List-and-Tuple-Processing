row = 3
cols = 5
tup = tuple([ ([0] * cols)for row in range(row)])
print(type(tup))
print(tup)
#second method
t = ((2,3,4),(5,6,7))
print(t)
print(t[0][2])