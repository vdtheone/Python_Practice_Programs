# Transpose a matrix

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i+1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))    