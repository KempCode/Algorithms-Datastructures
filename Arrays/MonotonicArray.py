#First Solution.... and O(1) space due to inplace comparisons.
# O(n) time because... isIncreasing shouldnt run till end of array and 
# isMonotonic will only run one of the loops!
def isIncreasing(array):
    # Loops through array and returns first instance of increasing or decreasing.
    for i in range(0, len(array)-1):
        if(array[i] < array[i+1]):
            return True
        elif(array[i] > array[i+1]):
            return False

def isMonotonic(array):
    # Edge cases of empty array and single digit.
    if(len(array) == 0 or len(array) == 1):
        return True
    # if it is monotonic - its entirely non increasing 
    if(isIncreasing(array) == True):
        for i in range(0,len(array)-1):
            if(array[i] <= array[i + 1]):
                continue
            else:
                return False
        return True
        
    else:
        # if it is monotonic - its entirely non decreasing 
        for i in range(0,len(array)-1):
            if(array[i] >= array[i + 1]):
                continue
            else:
                return False
        return True
  
    
# Second Solution
#O(n) time and O(1) space.
#Read hint 3 for this....

def isMonotonic(array):
    # Edge cases of empty array and single digit
    if(len(array) == 0 or len(array) == 1):
        return True

    isNonDecreasing = True
    IsNonIncreasing = True
    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            isNonDecreasing = False
        elif array[i] < array[i + 1]:
            IsNonIncreasing = False
    return isNonDecreasing or IsNonIncreasing
