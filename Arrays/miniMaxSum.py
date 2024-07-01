#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    output = []
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if(j != i):
                sum += arr[j]
        output.append(sum)
    print(min(output), max(output))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
