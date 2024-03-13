"""Sorted Squared Array Write a function that takes in a non-empty array of integers 
that are sorted in ascending order and returns a new array of the same length 
with the squares of the original integers also sorted in ascending order. 

Sample Input array = [1, 2, 3, 5,6,8,9]
Sample Output [1, 4, 9, 25, 36, 64, 81]"""


# Time complexity O(nlogn) Space complexity O(1)

def sortedSquaredArray(array):
    # Write your code here.
    for i in range(0, len(array)):
        print(array[i])
        array[i] = array[i] * array[i]
    # REMEMBER timsort has to be done in its own line and is O(nlogn)
    array.sort()
    return array




# O(n) time complexity O(n) Space complexity

def sortedSquaredArray(array):
    """Use two pointers to keep track of the smallest and largest values in the input array.
    Compare the absolute values of these smallest and largest values, square the larger absolute value,
    and place the square at the end of the output array, filling it up from right to left. 
    Move the pointers accordingly, and repeat this process until the output array is filled."""
    output_array = [0] * len(array)  # Preallocate output_array
    leftPos = 0
    rightPos = len(array) - 1

    for i in range(len(array)):
        left = array[leftPos]
        right = array[rightPos]

        if abs(left) > abs(right):
            # add right to left.
            output_array[len(array)- 1 - i] = left * left
            leftPos += 1
        else:
            output_array[len(array) - 1 - i] = right * right
            rightPos -= 1

    return output_array
