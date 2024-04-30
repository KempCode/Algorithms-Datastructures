# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class please
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # add the name of current element
        array.append(self.name)
        for i in self.children:
            # for each child recurse through and add name of current element
            i.depthFirstSearch(array)
        return array
