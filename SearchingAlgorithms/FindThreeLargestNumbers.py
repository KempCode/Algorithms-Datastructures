# Time O(N) space O(1)
# I really overcomplicated this before this simple solution.
def findThreeLargestNumbers(array):
    output = [float("-inf"), float("-inf"), float("-inf")]
    for i in range(len(array)):
        if array[i] > output[2]:
            # shift left.
            output[0] = output[1]
            output[1] = output[2]
            output[2] = array[i]
            
        elif array[i] > output[1]:
            # shift left
            output[0] = output[1]
            output[1] = array[i]
            
        elif array[i] > output[0]:
            output[0] = array[i]
           
            
    return output