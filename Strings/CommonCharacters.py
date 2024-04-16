# O(N*M) O(k), where k is the number of unique characters in all strings combined
def commonCharacters(strings):
    # first get all the unique characters from each string
    # this was my original way. less efficient
    #unique = []
    #for i in range(len(strings)):
    #    for j in strings[i]:
    #        if j not in unique:
    #            unique.append(j)
    #print(unique)

    # first get all the unique characters from each string
    unique = set()
    for string in strings:
        unique.update(set(string))
        
    output = []
    # then if the letter is commmon accross all sub strings we addit to output.
    for letter in unique:
        letter_counter = 0
        for string in strings:
            if letter in string: 
                letter_counter += 1
        if letter_counter == len(strings):
           output.append(letter)
    return output


