from ply import lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'elif': 'ELIF',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'def': 'DEF',
    'class': 'CLASS',
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

) + tuple(reserved.values())

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

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'

def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_NOT(t):
    'not'
    return t

def t_FLOAT(t):
    r'\d*\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno, t.value)
        t.value = 0.0
    return t

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno, t.value)
        t.value = 0
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_TRUE(t):
    r'True'
    t.value = True
    return t

def t_FALSE(t):
    r'False'
    t.value = False
    return t

def t_NONE(t):
    r'None'
    t.value = None
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print "Illegal charecter '%s'" % t.value[0]
    t.lexer.skip(1)

t_ignore = ' '

lexer = lex.lex()

