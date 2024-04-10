# O(n * m + n * m) time complexity and O(n * m + n * m) space complexity.
def transposeMatrix(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    output_matrix =[]

    # THE TRICKY PART IN THIS IS NOT THE TRANSPOSING BUT SETTING UP DEFAULT VALUES IN PYTHON.
    for i in range(col_len):
        output_matrix.append([0] * row_len)
        
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            output_matrix[j][i] = matrix[i][j] 
    return output_matrix



# O(n * m) time complexity and O(n * m) space complexity.
# inline though this time..
def transposeMatrix(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    output_matrix = []

    # loop through columns 
    for i in range(0, col_len):
        new_row = []
        for j in range(0, row_len):
            # add column values to new row..
            new_row.append(matrix[j][i])
        output_matrix.append(new_row)
    return output_matrix