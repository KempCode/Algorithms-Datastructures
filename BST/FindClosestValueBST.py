def findClosestValueInBst(tree, target):
    closest = float("inf")
    while tree is not None:
        diff_closest = abs(closest - target)
        diff_current_node = abs(tree.value - target)

        if diff_current_node < diff_closest:
            # current node is closer to target than previous closest. Update closest to current value
            closest = tree.value
        # ^ else closest remains same.

        # find next value
        # if current node is less than target go right
        elif tree.value < target:
            tree = tree.right
        # if current node is more than target go left
        elif tree.value > target:
            tree = tree.left
        elif tree.value == target:
            # if tree.value / current_node is == targrt
            break
    return closest
        
        

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
