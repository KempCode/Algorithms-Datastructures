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
