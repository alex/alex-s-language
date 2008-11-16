from alexs_lang.parser import Parser

from alexs_lang import ast

class ContextDictionary(object):
    def __init__(self):
        self._contexts = [{}]
    
    def __setitem__(self, key, val):
        self._locals[key] = val
    
    def __getitem__(self, key):
        try:
            return self._locals[key]
        except KeyError:
            return self._globals[key]
    
    def __contains__(self, key):
        return key in self._locals or key in self._globals
    
    @property
    def is_global(self):
        return len(self._contexts) > 1
    
    @property
    def _locals(self):
        return self._contexts[len(self._contexts)-1]
    
    @property
    def _globals(self):
        return self._contexts[0]
    
    def enter_local(self):
        self._contexts.append({})
    
    def leave_local(self):
        self._contexts.pop()

class PrintFunction(ast.FunctionBody):
    def __init__(self):
        pass
    
    def calculate(self, args, context):
        print args[0]

class RangeFunction(ast.FunctionBody):
    def __init__(self):
        pass
    
    def calculate(self, arg, context):
        return range(*arg)

class Interpreter(object):
    def __init__(self, code):
        self.code = code
        self.context = ContextDictionary()
        self.context['print'] = PrintFunction()
        self.context['range'] = RangeFunction()
    
    def execute(self):
        self.parse()
        self.ast.calculate(self.context)
    
    def parse(self):
        self.parser = Parser()
        self.ast = self.parser.parse(self.code)
