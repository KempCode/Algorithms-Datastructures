def longestPeak(array):
    # Write your code here.
    highest_peak = 0
    current_peak = 1
    # could be increasing, decreasing or neither.
    increasing = False
    decreasing = False
    
    for i in range(0, len(array)-1):
        
        if((array[i] < array[i+1]) and (decreasing == False)):
            # could be previously increasing or from beginning, now increasing
            current_peak += 1
            increasing = True
            
        elif((array[i] > array[i+1]) and (increasing == True)):
            # previously increasing and starts to decrease.. breaks the current peak
            current_peak += 1
            decreasing = True
            
            highest_peak= max(highest_peak, current_peak)
        elif(array[i] == array[i+1]):
            # reset
            current_peak = 1
            increasing = False
            decreasing = False
        elif(array[i] < array[i+1] and decreasing == True):
            # previously decreasing and starts to increase
            """we set current_peak to 2 to account for the two elements (array[i] and array[i+1]) 
            that we've encountered so far in the increasing sequence.
            E.g., example 1 where i is 0 and i+1 is 10... 0 is included in the peak."""
            current_peak = 2
            increasing = True
            decreasing = False
        

    return highest_peak
        
    