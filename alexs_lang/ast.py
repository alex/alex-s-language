class Node(object):
    def __init__(self, type_, children = None, leaf = None):
        self.type = type_
        if children is None:
            children = []
        self.children = children
        self.leaf = leaf
