# Brute force approach O(N^2) Time O(1) space
def firstNonRepeatingCharacter(string):
 
    for i in range(len(string)):
        current_char = i
        repeating = False
        
        for j in range(len(string)):
            
            if i != j and string[i] == string[j]:
                repeating = True
                break
                
        if repeating is False:
            return current_char
        
    return -1


#O(N) time O(1) space best case O(N) worst Case.

def firstNonRepeatingCharacter(string):
    my_dict = {}
    for i in range(len(string)):
        if string[i] in my_dict:
            # mydict{"a":(position, character frequency)}
            my_dict[string[i]] = (my_dict[string[i]][0], my_dict[string[i]][1] + 1)
        else:
            my_dict[string[i]] = (i,1)

    # They chars are added in order they are found in original array, but we still need original index hence the 
    # Tuple
    for i in my_dict:
        if my_dict[i][1] == 1:  
            return my_dict[i][0] #return stored position of char from original array
     
    return -1
