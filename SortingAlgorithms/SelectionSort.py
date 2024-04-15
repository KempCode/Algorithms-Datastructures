#https://www.youtube.com/watch?v=g-PGLbMth_g&ab_channel=MichaelSambol
# left inplace array is sorted, right is not
# Worse big O time than bubble or insertion, its O(N^2) across worst, average and best cases. 
# O(1) space, as its done inline.
def selectionSort(array):
    for i in range(len(array)):
        current_min_pos = i
        for j in range(i, len(array)):
            if(array[j] < array[current_min_pos]):
                current_min_pos = j
        # swap with current minimum with i (first element of right array)
        temp = array[i]
        array[i] = array[current_min_pos]
        array[current_min_pos] = temp
    return array    
