from itertools import count

from alexs_lang.compile import ContextVars

CODE_TEMPLATE = """
#include "src/base.cpp"

%(functions)s

int main() {
    AlObj* print = new AlPrint();
    %(main)s
}
"""

def get_unused_name(context):
    for i in count():
        if "t%s" % i not in context:
            return "t%s" % i

class Generator(object):
    def __init__(self, ast):
        self.ast = ast
        self.context = ContextVars()
        self.context.add('print')
    
    def generate(self):
        gen = self.ast.generate(CPP_GENERATORS)
        functions, main = gen.as_code(self.context)
        return CODE_TEMPLATE % {'functions': functions if functions else '', 'main': '\n'.join(main)}

class NodeListGenerator(object):
    def __init__(self, nodes):
        self.nodes = nodes
    
    def as_code(self, context):
        functions, main = [], []
        for node in self.nodes:
            f, m = node.as_code(context)
            functions.extend(f)
            main.extend(m)
        return functions, ['%s;' % x for x in main]

class BinaryOpGenerator(object):
    OPS = {
        '+': '+',
        '-': '-',
        '*': '*',
        '/': '/',
        '**': None,
        '==': '==',
        '!=': '!=',
        '>': '>',
        '<': '<',
        '>=': '>=',
        '<=': '<=',
        'and': '&&',
        'or': '||',
    }
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
        
    def as_code(self, context):
        return [], ["*(%s) %s %s" % ('\n'.join(self.left.as_code(context)[1]), self.OPS[self.op], '\n'.join(self.right.as_code(context)[1]))]

class IntegerGenerator(object):
    def __init__(self, value):
        self.value = value
    
    def as_code(self, context):
        return [], ["new AlInt(%s)" % self.value]

class FunctionCallGenerator(object):
    def __init__(self, name, arglist):
        self.name = name
        self.arglist = arglist
    
    def as_code(self, context):
        main = []
        varname = get_unused_name(context)
        main.append("ARG_TYPE %s" % varname)
        for arg in self.arglist:
            main.append("%s.push_back(%s)" % (varname, '\n'.join(arg.as_code(context)[1])))
        main.append('(*%s)(%s, KWARG_TYPE())' % ('\n'.join(self.name.as_code(context)[1]), varname))
        return [], main

class NameGenerator(object):
    def __init__(self, name):
        self.name = name
    
    def as_code(self, context):
        return [], [self.name]

CPP_GENERATORS = {
    'node_list': NodeListGenerator,
#    'function': FunctionGenerator,
    'binary_op': BinaryOpGenerator,
#    'unary_op': UnaryOpGenerator,
    'int': IntegerGenerator,
#    'bool': BooleanGenerator,
#    'none': NoneGenerator,
#    'assign': AssignmentGenerator,
    'name': NameGenerator,
#    'if': IfGenerator,
    'function_call': FunctionCallGenerator,
#    'return': ReturnGenerator,
}

