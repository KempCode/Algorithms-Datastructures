def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    current_closest_diff = 999
    array1Count = 0
    array2Count = 0
    output_array = [0,0]

    while array1Count < len(arrayOne) and array2Count < len(arrayTwo):
        difference = abs(arrayOne[array1Count] - arrayTwo[array2Count])

        if(difference == 0):
            #exact match difference is 0
            current_closest_diff = difference
            return [arrayOne[array1Count], arrayTwo[array2Count]]
            
        if(difference < current_closest_diff):
            # if current is better then keep current.
            current_closest_diff = difference
            output_array = [arrayOne[array1Count], arrayTwo[array2Count]]

        #increment counter for the smaller number in corresponding array.
        if(arrayOne[array1Count] > arrayTwo[array2Count]):
            array2Count += 1
        elif(arrayOne[array1Count] < arrayTwo[array2Count]):
            array1Count += 1
        
    return output_array
