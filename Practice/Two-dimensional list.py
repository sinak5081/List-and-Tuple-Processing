matrix = [[j for j in range(7)]for i in range(4)]
print("number of rows:",len(matrix))
print("number of cols:",len(matrix[0]))
print("contents of matrix")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()
print("__________________________________________")
#Second method
row = 4
cols = 7
twoDim = [ ([0] * cols) for row in range(row)]
print("Number of rows:",len(twoDim))
print("Number of columns:",len(twoDim[1]))
for i in range(len(twoDim)):
    for j in range(len(twoDim[0])):
        print(twoDim[i][j],end=" ")
    print()
print("__________________________________________")
#third method
mat = [[1,2,3], [4,5,6]]
print(mat)