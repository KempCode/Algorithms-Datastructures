# O(nlogn) time O(1) space. n is number of coins.

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    # current change we can store up to.
    change = 0
# if we ever hit a coin that has a value that is > current_change + 1 - cant make this change..
# if i is <= our change + 1 we can make the change
    for i in coins:
        if(i > change + 1):
            # cant make the change
            # return lowest amount of change we can make + 1 (it is lowest amount of change we cant make.)
            return change + 1
        else:
            # can make the change - add to previous change
            change += i
    return change + 1 
    #(it is lowest amount of change we cant make.)
                
            
  
