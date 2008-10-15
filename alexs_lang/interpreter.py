from alexs_lang.parser import Parser

from alexs_lang import ast

class ContextDictionary(object):
    def __init__(self):
        self._local = {}
        self._global = {}
        self._locals = []
    
    def __setitem__(self, key, val):
        if not self._locals:
            self._global[key] = val
        else:
            self._local[key] = val
    
    def __getitem__(self, key):
        if self._locals and key in self._local:
            return self._local[key]
        return self._global[key]
    
    def __contains__(self, key):
        if self._locals and key in self._local:
            return True
        return key in self._global
    
    def enter_local(self):
        self._locals.append(self._local)
        self._local = {}
    
    def leave_local(self):
        self._local = self._locals.pop()

class PrintFunction(ast.FunctionBody):
    def __init__(self):
        pass
    
    def calculate(self, args, context):
        print args[0]

class Interpreter(object):
    def __init__(self, code):
        self.code = code
        self.context = ContextDictionary()
        self.context['print'] = PrintFunction()
    
    def execute(self):
        self.parse()
        for node in self.ast:
            node.calculate(self.context)
    
    def parse(self):
        self.parser = Parser()
        self.ast = self.parser.parse(self.code)
