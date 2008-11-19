from itertools import count

from alexs_lang.compile import ContextVars

class NoSemi(str):
    no_semi = True

CODE_TEMPLATE = """#include "src/base.h"

%(functions)s
int main() {
    %(main)s
}
"""

def get_unused_name(context, prefix='t'):
    for i in count():
        if "%s%s" % (prefix, i) not in context:
            return "%s%s" % (prefix, i)

class Generator(object):
    def __init__(self, ast):
        self.ast = ast
        self.context = ContextVars()
        self.context.add('print')
    
    def generate(self):
        gen = self.ast.generate(CPP_GENERATORS)
        functions, main = gen.as_code(self.context)
        return CODE_TEMPLATE % {'functions': '\n'.join(functions) if functions else '', 'main': '\n'.join(main)}

class NodeListGenerator(object):
    def __init__(self, nodes):
        self.nodes = nodes
    
    def as_code(self, context):
        functions, main = [], []
        for node in self.nodes:
            f, m = node.as_code(context)
            functions.extend(f)
            main.extend(m)
        return functions, ['%s%s' % (x, ';' if not getattr(x, 'no_semi', False) else '') for x in main]

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
        main = self.left.as_code(context)[1]
        left = main.pop()
        main.extend(self.right.as_code(context)[1])
        right = main.pop()
        main.append("(*(%s)) %s %s" % (left, self.OPS[self.op], right))
        return [], main

class IntegerGenerator(object):
    def __init__(self, value):
        self.value = value
    
    def as_code(self, context):
        return [], ["(AlObj*)(new AlInt(%s))" % self.value]

class FunctionCallGenerator(object):
    def __init__(self, name, arglist):
        self.name = name
        self.arglist = arglist
    
    def as_code(self, context):
        main = []
        varname = get_unused_name(context)
        main.append("ARG_TYPE %s" % varname)
        context.add(varname)
        for arg in self.arglist:
            main.extend(arg.as_code(context)[1])
            main.append("%s.push_back(%s)" % (varname, main.pop()))
        main.append('(*%s)(%s, KWARG_TYPE())' % (self.name.as_code(context)[1][0], varname))
        return [], main

class NameGenerator(object):
    def __init__(self, name):
        self.name = name
    
    def as_code(self, context):
        return [], [self.name]

class AssignmentGenerator(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def as_code(self, context):
        func, main = self.right.as_code(context)
        if isinstance(self.right, FunctionGenerator):
            right = func.pop()
        else:
            right = main.pop()
        for left in self.left:
            if left.as_code(context)[1][0] in context:
                if isinstance(self.right, FunctionGenerator):
                    func.append('%s = %s;' % (left.as_code(context)[1][0], right))
                else:
                    main.append('%s = %s;' % (left.as_code(context)[1][0], right))
            else:
                context.add(left.as_code(context)[1][0])
                if isinstance(self.right, FunctionGenerator):
                    func.append('AlObj* %s = %s;' % (left.as_code(context)[1][0], right))
                else:
                    main.append('AlObj* %s = %s;' % (left.as_code(context)[1][0], right))
        return func, main

class FunctionGenerator(object):
    def __init__(self, args, body):
        self.args = args
        self.body = body
    
    def as_code(self, context):
        function = """class %(fname)s : public AlFunction {
            public:
                virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
                    %(args)s
                    %(body)s
                }
        };
        """
        fname = get_unused_name(context, 'f')
        context.enter_local()
        args = []
        for arg in reversed(self.args):
            args.append('AlObj* %s = args.back();' % arg)
            args.append('args.pop_back();')
        body = self.body.as_code(context)[1]
        return [function % {'fname': fname, 'args': '\n'.join(args), 'body': '\n'.join(body)}, "new %s()" % fname], []

class ReturnGenerator(object):
    def __init__(self, value):
        self.value = value
    
    def as_code(self, context):
        main = self.value.as_code(context)[1]
        main.append('return %s' % main.pop())
        return [], main

class IfGenerator(object):
    def __init__(self, condition, body, else_body, elifs):
        self.condition = condition
        self.body = body
        self.else_body = else_body
        self.elifs = elifs
    
    def as_code(self, context):
        funcs, main = [], []
        main.extend(self.condition.as_code(context)[1])
        main.append(NoSemi("if (bool(%s)) {" % main.pop()))
        main.extend(self.body.as_code(context)[1])
        main.append(NoSemi("}"))
        if self.elifs is not None:
            for cond, body in self.elifs:
                main.extend(cond.as_code(context)[1])
                main.append(NoSemi("else if (%s) {" % main.pop()))
                main.extend(self.body.as_code(context)[1])
                main.append(NoSemi("}"))
        if self.else_body is not None:
            main.append(NoSemi("else {"))
            main.extend(self.else_body.as_code(context)[1])
            main.append(NoSemi("}"))
        return funcs, main

CPP_GENERATORS = {
    'node_list': NodeListGenerator,
    'function': FunctionGenerator,
    'binary_op': BinaryOpGenerator,
#    'unary_op': UnaryOpGenerator,
    'int': IntegerGenerator,
#    'bool': BooleanGenerator,
#    'none': NoneGenerator,
    'assign': AssignmentGenerator,
    'name': NameGenerator,
    'if': IfGenerator,
    'function_call': FunctionCallGenerator,
    'return': ReturnGenerator,
}

