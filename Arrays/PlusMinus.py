#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos_count += 1
        if arr[i]  < 0:
            neg_count += 1
        if arr[i] == 0:
            zero_count += 1
    
    pos_ratio = pos_count / len(arr)
    neg_ratio = neg_count / len(arr)
    zero_ratio = zero_count / len(arr)
    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))
   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
