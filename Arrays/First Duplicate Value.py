# ON^2 Time and O(1) Space 
def firstDuplicateValue(array):
    minimum_duplicate_index = None  # Initialize to None

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:  # Found a duplicate
                if minimum_duplicate_index is None or j < minimum_duplicate_index:
                    minimum_duplicate_index = j  # Update to the index of the duplicate
                break  # Found a duplicate, no need to check further for this i

    # Return the first duplicate value or -1 if none found
    if minimum_duplicate_index is not None:
        return array[minimum_duplicate_index]
    else:
        return -1




#O(N) time and O(N) Space
def firstDuplicateValue(array):
    myset = set()
    for i in range(len(array)):
        if(array[i] in myset):
            return array[i]
        myset.add(array[i])
    return -1
        
        