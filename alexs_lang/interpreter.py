from alexs_lang.parser import Parser

class Interpreter(object):
    def __init__(self, code):
        self.code = code
        self.context = {}
    
    def execute(self):
        self.parse()
        for node in self.ast:
            print node.calculate(self.context)
    
    def parse(self):
        self.parser = Parser()
        self.ast = self.parser.parse(self.code)
