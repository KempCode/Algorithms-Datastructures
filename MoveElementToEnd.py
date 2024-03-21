def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) -1
    # Left and right pointers to end of list. Going inward swapping  if needed
    while(left < right):
        if(array[right] == toMove):
            right -= 1
        elif(array[right] != toMove and array[left] == toMove):
            # Swap
            temp = array[right]
            array[right] = array[left]
            array[left] = temp
        elif(array[left] != toMove):
            left += 1
    return array
