from alexs_lang.parser import Parser

from alexs_lang import ast

class ContextVars(object):
    def __init__(self):
        self._contexts = [set()]
    
    def __contains__(self, key):
        return key in self._locals or key in self._globals
    
    def add(self, key):
        self._locals = key
    
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
        self._contexts.append(set())
    
    def leave_local(self):
        self._contexts.pop()

class Compiler(object):
    def __init__(self, code):
        self.code = code
        self.context = ContextVars()
    
    def compile(self):
        self.parse()
    
    def parse(self):
        self.parser = Parser()
        self.ast = self.parser.parse(self.code)
