import math

Matrix = [
    #1  2  3  4  5
    [0, 1, 0, 0, 3], #1
    [0, 0, 8, 7, 1], #2
    [0, 0, 0, 1, -5],#3
    [0, 0, 2, 0, 0], #4
    [0, 0, 0, 4, 0]  #5
]

n = len(Matrix)
MatrixTransformations = []

firstLine = [0]
for firstEl in range(n-1):
    firstLine.append(math.inf)

MatrixTransformations.append(firstLine)

for line in range(n):
   for i in range(len(Matrix[line])):
        if Matrix[line][i] == 0:
            Matrix[line][i] = math.inf

k = 1
while k < n:
    line = []
    for i in range(n):
        Ui = MatrixTransformations[k-1][i]
        for j in range(n):
            if Ui > MatrixTransformations[k-1][j] + Matrix[j][i]:
                Ui = MatrixTransformations[k-1][j] + Matrix[j][i]
        line.append(Ui)
    MatrixTransformations.append(line)
    k+=1

for i in range(1, n):
    print(f"Кратчайший путь до верщины {i+1} = {MatrixTransformations[k-1][i]}")
