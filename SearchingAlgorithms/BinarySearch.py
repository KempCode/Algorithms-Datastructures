def binarySearch(array, target):
    left = 0
    right = len(array) -1
    # while the left and right pointers dont cross, ie. havent gone through every item in array
    while(left <= right):
        middle = (left + right) // 2
        if(array[middle] == target):
            return middle
        elif(array[middle] > target):
            right = middle -1
            # move right left of current middle because middle value explicitly > target
        elif(array[middle] < target):
            left = middle + 1
    return -1
        
    
