# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier=1):
    sum = 0
    for i in array:
        if type(i) is list :
            # if its a list recurse through, adding to the multiplier every depth increase
            sum += productSum(i, multiplier + 1)
        else:
            # if its just a number not a list add it to the sum.
            sum += i
    # return the sum * multiplier. (outer array is 1).. for inner arrays weve been += 1 every depth.
    return sum * multiplier
        
