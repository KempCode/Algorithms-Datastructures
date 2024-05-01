def getPermutations(array):
    # Write your code here.
    output = []
    permutations_helper(array, 0, output)
    return output

def permutations_helper(array, i, output):
    if i == len(array) - 1:
        output.append(array[:])
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            permutations_helper(array, i + 1, output)
            array[i], array[j] = array[j], array[i]  # backtrack

# Function test
print(getPermutations([1, 2, 3]))
print(getPermutations([1, 5, 6, 7, 9]))