import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#input is a 2d array.
#1 2 3
#4 5 6
#9 8 9
# abs((1+5+9)-(3+5+9))
# abs(15-17) = 2
def diagonalDifference(arr):
    left_diag_sum = 0
    right_diag_sum = 0
    
    for i in range(len(arr)):
        left_diag_sum += arr[i][i]           # Left diagonal (top-left to bottom-right)
        right_diag_sum += arr[i][len(arr) - 1 - i]  # Right diagonal (top-right to bottom-left)
        
    return abs(left_diag_sum - right_diag_sum)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
