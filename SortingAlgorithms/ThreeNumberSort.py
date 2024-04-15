# O(N) time- 3 for loops so 3N - ignore constant, O(1) space as in place.
def threeNumberSort(array, order):
    zero_array_tracker = 0
    one_array_tracker = 0
    three_array_tracker = 0
    
    for i in range(len(array)):
        if(array[i] == order[0]):
            temp = array[i]
            array[i] = array[zero_array_tracker]
            array[zero_array_tracker] = temp
            zero_array_tracker += 1
    
    one_array_tracker = zero_array_tracker
    for i in range(len(array)):
        if(array[i] == order[1]):
            temp = array[i]
            array[i] = array[one_array_tracker]
            array[one_array_tracker] = temp
            one_array_tracker += 1
            
    two_array_tracker = one_array_tracker
    for i in range(len(array)):
        if(array[i] == order[2]):
            temp = array[i]
            array[i] = array[two_array_tracker]
            array[two_array_tracker] = temp
            two_array_tracker += 1
            
    return array



# O(N) time- 3 for loops so 3N - ignore constant, O(1) space as in place.
# Technically you only need two loops as if order[0] and order[1] are in order the only things remaining
# will be order[2] elements in array at the very end lol
def threeNumberSort(array, order):
    zero_array_tracker = 0
    one_array_tracker = 0
    
    for i in range(len(array)):
        if(array[i] == order[0]):
            temp = array[i]
            array[i] = array[zero_array_tracker]
            array[zero_array_tracker] = temp
            zero_array_tracker += 1
    
    one_array_tracker = zero_array_tracker
    for i in range(len(array)):
        if(array[i] == order[1]):
            temp = array[i]
            array[i] = array[one_array_tracker]
            array[one_array_tracker] = temp
            one_array_tracker += 1
            
    return array

