# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = []
        # add root node into queue
        queue.insert(0,self)

        while len(queue) > 0:
            # pop from queue
            # add to output array.
            current_node = queue.pop()
            array.append(current_node.name)
            # traverse children
            for i in current_node.children:
                queue.insert(0,i)

        return array
