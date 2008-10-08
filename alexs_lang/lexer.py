from ply import lex

def track_indents(lexer):
    while True:
        token = lexer.token()
        if token is not None:
            yield token
        else:
            break

class Lexer(object):
    def __init__(self):
        self._built = False
    
    def require_built(self):
        if not self._built:
            self.build()
    
    def build(self, **kwargs):
        self.lexer = lex.lex(object=self, **kwargs)
    
    def input(self, s):
        self.require_built()
        self.lexer.paren_count = 0
        self.lexer.input(s)
        self.token_stream = track_indents(self.lexer)
    
    def token(self):
        try:
            return self.token_stream.next()
        except StopIteration:
            return None
        
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'elif': 'ELIF',
        'while': 'WHILE',
        'for': 'FOR',
        'in': 'IN',
        'def': 'DEF',
        'class': 'CLASS',
        'return': 'RETURN',
        'break': 'CONTINUE',
    }
    tokens = (
        # objects of sorts
        'NAME',
        
        'FLOAT',
        'INTEGER',
        'TRUE',
        'FALSE',
        'NONE',
        
        # operators
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'MODULO',
        'POWER',
        'NOT',
        
        # assignment
        'EQUALS',
        'PLUS_EQUALS',
        'MINUS_EQUALS',
        'TIMES_EQUALS',
        'DIVIDE_EQUALS',
        
        # comparisons
        'EQ',
        'LT',
        'GT',
        'LE',
        'GE',
        'AND',
        'OR',
        
        # syntax
        'LPAREN',
        'RPAREN',
        'COMMENT',
        'COLON',
        'COMMA',
        
        'WHITESPACE',
        'NEWLINE',
    ) + tuple(reserved.values())

    t_ignore = ' '

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MODULO = r'%'
    t_POWER = r'\*\*'

    t_EQUALS = r'='
    t_PLUS_EQUALS = r'\+='
    t_MINUS_EQUALS = r'-='
    t_TIMES_EQUALS = r'\*='
    t_DIVIDE_EQUALS = r'/='

    t_EQ = r'=='
    t_LT = r'<'
    t_GT = r'>'
    t_LE = r'<='
    t_GE = r'>='

    t_COLON = r':'
    
    def t_WHITESPACE(self, t):
        r' [ ]+ '
        if t.lexer.at_line_start and not t.lexer.paren_count:
            return t
    
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.type = 'NEWLINE'
        if not t.lexer.paren_count:
            return t
    
    def t_LPAREN(self, t):
        r'\('
        t.lexer.paren_count += 1
        return t
    
    def t_RPAREN(self, t):
        r'\)'
        t.lexer.paren_count -= 1
        return t
    
    def t_AND(self, t):
        r'and'
        return t

    def t_OR(self, t):
        r'or'
        return t

    def t_NOT(self, t):
        'not'
        return t

    def t_FLOAT(self, t):
        r'\d*\.\d+'
        try:
            t.value = float(t.value)
        except ValueError:
            print "Line %d: Number %s is too large!" % (t.lineno, t.value)
            t.value = 0.0
        return t

    def t_INTEGER(self, t):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print "Line %d: Number %s is too large!" % (t.lineno, t.value)
            t.value = 0
        return t

    def t_TRUE(self, t):
        r'True'
        t.value = True
        return t

    def t_FALSE(self, t):
        r'False'
        t.value = False
        return t

    def t_NONE(self, t):
        r'None'
        t.value = None
        return t

    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'NAME')
        return t

    def t_COMMENT(self, t):
        r'\#.*'
        pass

    def t_error(self, t):
        print "Illegal charecter '%s'" % t.value[0]
        t.lexer.skip(1)
    
