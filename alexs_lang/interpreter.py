from alexs_lang.parser import Parser

from alexs_lang import ast

class PrintFunction(ast.Function):
    def __init__(self):
        pass
    
    def calculate(self, context):
        print context[0]

class Interpreter(object):
    def __init__(self, code):
        self.code = code
        self.context = {}
        self.context['print'] = PrintFunction()
    
    def execute(self):
        self.parse()
        for node in self.ast:
            node.calculate(self.context)
    
    def parse(self):
        self.parser = Parser()
        self.ast = self.parser.parse(self.code)
