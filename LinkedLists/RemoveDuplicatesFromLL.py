# since LL is in sorted order, if the next item is equal to current item remove the current.
# O(n) time due to one loop through LL and O(1) space due to whole thing done in place....
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    current_item = linkedList # not linkedList.value, it should be equal to the node and can access 2 properties
    while(current_item is not None and current_item.next is not None):
        next_node = current_item.next
        
        if(current_item.value == next_node.value):
            # skip the duplicate node
            current_item.next = next_node.next
        else:
            #normal case
            current_item = next_node
    return linkedList
