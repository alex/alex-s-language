class Node(object):
    def __init__(self, type_, children = None, leaf = None):
        self.type = type_
        if children is None:
            children = []
        self.children = children
        self.leaf = leaf

class Expression(object):
    pass

class BinaryOperation(Expression):
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

class UnaryOperation(Expression):
    def __init__(self, value, op):
        self.value = value
        self.op = op

class Number(Expression):
    def __init__(self, value):
        self.value = value

class Comparison(Expression):
    def __init__(self, left, right, comp):
        self.left = left
        self.right = right
        self.comp = comp

class Assignment(Expression):
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
