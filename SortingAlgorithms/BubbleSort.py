def bubbleSort(array):
    for k in range(len(array)-1):
        # The important part here is
        # made_swaps = False BEFORE the loop through
        # if no swaps have been made then its in order.
        made_swaps = False
        for i in range(len(array) - 1):
            if(array[i] >= array[i+1]):
                # swap
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
                made_swaps = True
        if(made_swaps == False):
            break
    return array