# My favourite solution:
def insertionSort(array):
    # Write your code here.
    for i in range(len(array)):
        # loop from beginning of left array and
        # insert i into correct point of left array
            # do this by swapping from current pos i left until in right spot.

        # IMPORTANT - REMEMBER REVERSED DOESNT ACTUALLY ITERATE BACKWARDS, ESSENTIALLY DOES IT NORMALLY AND PRINTS
        # BACKWARD, whereas range actually decrements like C++
        # this range goes down to 0 but not including
        for j in (range(i, 0, -1)):
            if(array[j] < array[j-1]):
                # swap
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp

    return array
            



# This version explains the difference of a range decrement loop and reversed.()
# I prefer the other way, in reverse() you have to do your operations left to right and then
# The reversed() iterator will return it all backwards at the very end.!!

def insertionSort(array):
    for i in range(len(array)):
        for j in reversed(range(i)):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
