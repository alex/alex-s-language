import operator

class NodeList(object):
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children
    
    def append(self, val):
        self.children.append(val)
    
    def __str__(self):
        return '\n'.join(str(x) for x in self)
    
    def __iter__(self):
        return iter(self.children)
    
    def calculate(self, context):
        for node in self.children:
            node.calculate(context)

class Expression(object):
    def calculate(self):
        raise NotImplementedError()

class BinaryOperation(Expression):
    OPS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div,
        '==': operator.eq,
        '!=': operator.ne,
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        'and': operator.and_,
        'or': operator.or_,
    }
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    
    def __str__(self):
        return "<BinaryOperation: %s %s %s>" % (self.left, self.op, self.right)
    
    def calculate(self, context):
        return self.OPS[self.op](self.left.calculate(context), self.right.calculate(context))

class UnaryOperation(Expression):
    OPS = {
        '-': operator.neg,
        '+': operator.pos,
        'not': operator.not_,
    }
    def __init__(self, value, op):
        self.value = value
        self.op = op
    
    def __str__(self):
        return "<UnaryOperation: %s %s>" % (self.op, self.value)
    
    def calculate(self, context):
        return self.OPS[self.op](self.value.calculate(context))

class Number(Expression):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "<Number: %s>" % self.value
    
    def calculate(self, context):
        return self.value

class Boolean(Expression):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "<Boolean: %s>" % self.value
    
    def calculate(self, context):
        return self.value

class NoneVal(Expression):
    def __str__(self):
        return "<None>"
    
    def calculate(self, context):
        return None

class Assignment(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return "<Assignment: %s = %s>" % (self.left, self.right)
    
    def calculate(self, context):
        val = self.right.calculate(context)
        for var in self.left:
            context[var.name] = val

class Name(Expression):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "<Name: %s>" % self.name
    
    def calculate(self, context):
        return context[self.name]

class If(NodeList):
    def __init__(self, condition, main_body, else_body=None):
        self.condition = condition
        self.main_body = main_body
        self.else_body = else_body
    
    def __str__(self):
        return "<If: %s>" % self.condition
    
    def calculate(self, context):
        if self.condition.calculate(context):
            return self.main_body.calculate(context)
        elif self.else_body is not None:
            return self.else_body.calculate(context)

class FunctionCall(Expression):
    def __init__(self, name, arglist):
        self.name = name
        self.arglist = arglist
    
    def __str__(self):
        return "<FunctionCall: %s(%s)>" % (self.name, ', '.join(self.arglist))
    
    def calculate(self, context):
        self.name.calculate(context).calculate([x.calculate(context) for x in self.arglist])

class Function(Expression):
    def __init__(self, args, body):
        self.args = args
        self.body = body
    
    def __str__(self):
        return "<Function:>"
    
    def calculate(self, context):
        return self.body.calculate(dict(zip(args, context)))
