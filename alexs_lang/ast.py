class NodeList(object):
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children
    
    def append(self, val):
        self.children.append(val)
    
    def __str__(self):
        return '\n'.join(str(x) for x in self.children)

class Expression(object):
    pass

class BinaryOperation(Expression):
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    
    def __str__(self):
        return "<BinaryOperation: %s %s %s>" % (self.left, self.op, self.right)

class UnaryOperation(Expression):
    def __init__(self, value, op):
        self.value = value
        self.op = op
    
    def __str__(self):
        return "<UnaryOperation: %s %s>" % (self.op, self.value)

class Number(Expression):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "<Number: %s>" % self.value

class Boolean(Expression):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "<Boolean: %s>" % self.value

class NoneVal(Expression):
    def __str__(self):
        return "<None>"

class Comparison(Expression):
    def __init__(self, left, right, comp):
        self.left = left
        self.right = right
        self.comp = comp
    
    def __str__(self):
        return "<Comparison: %s %s %s>" % (self.left, self.comp, self.right)

class Assignment(Expression):
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    
    def __str__(self):
        return "<Assignment: %s %s %s>" % (self.left, self.op, self.right)

class Name(Expression):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "<Name: %s>" % self.name
