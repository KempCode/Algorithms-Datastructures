# time is O(n) loop through twice O(1) space.. only storing variables
# This is an input class. Do not edit.
# Odd length LL its the middle number found by integer division // 2 
# and same with even length LL but it will be 2nd of the two middle nodes

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # loop through to learn the length first
    ll_len = 0
    current_node = linkedList
    while(current_node != None):
        next_node = current_node.next
        #print(current_node.value)
        ll_len += 1
        current_node = next_node
        
    print("length is", str(ll_len))
    # loop until middle node and return the middle node.
    counter = 0
    middle_node = linkedList
    while(counter < ll_len // 2):
        middle_node = middle_node.next
        counter += 1
    return middle_node
       
    




    