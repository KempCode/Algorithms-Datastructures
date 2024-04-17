# O(n*m) time and O(1) space
def searchInSortedMatrix(matrix, target):
    result = [None,None]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == target):
                result[0] = i
                result[1] = j
                return result
    return [-1,-1]
            

# The key to the more efficient solution of O(N + M) instead of O(N*M) lies in the
# fact that its a sorted matrix
def searchInSortedMatrix(matrix, target):
    # start at top right column then:
        # loop until we reach max rows or reach lower than the first column
            # i current is greater than target reduce column
            # if the current is less than target increase row
    i = 0
    j = len(matrix[0]) - 1
    
    while i <= len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return [i,j]
        elif matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
    return [-1,-1]


        
    
