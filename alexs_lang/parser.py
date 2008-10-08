#!/usr/bin/env python

import operator

from ply import yacc

from lexer import Lexer

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
    ('left', 'POWER'),
)

BINARY_OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '%': operator.mod,
    '**': operator.pow,
}

UNARY_OPS = {
    '+': operator.pos,
    '-': operator.neg,
    'not': operator.not_
}

COMPARISON_OPS = {
    '==': operator.eq,
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    'and': operator.and_,
    'or': operator.or_,
}

names = {}

def p_statement_assign(t):
    '''
    statement : NAME EQUALS expression
              | NAME PLUS_EQUALS expression
              | NAME MINUS_EQUALS expression
              | NAME TIMES_EQUALS expression
              | NAME DIVIDE_EQUALS expression
    '''
    if t[2] == '=':
        names[t[1]] = t[3]
    elif t[2] == '+=':
        names[t[1]] += t[3]
    elif t[2] == '-=':
        names[t[1]] -= t[3]
    elif t[2] == '*=':
        names[t[1]] *= t[3]
    elif t[2] == '/=':
        names[t[1]] /= t[3]

def p_statement_expr(t):
    '''
    statement : expression
    '''
    t[0] = t[1]
    print t[0]

def p_expression_binop(t):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression MODULO expression
               | expression POWER expression
    '''
    t[0] = BINARY_OPS[t[2]](t[1], t[3])

def p_expression_unaryop(t):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
               | NOT expression
    '''
    t[0] = UNARY_OPS[t[1]](t[2])

def p_expression_group(t):
    '''
    expression : LPAREN expression RPAREN
    '''
    t[0] = t[2]

def p_expression_compare(t):
    '''
    expression : expression EQ expression
               | expression LT expression
               | expression GT expression
               | expression LE expression
               | expression GE expression
               | expression AND expression
               | expression OR expression
    '''
    t[0] = COMPARISON_OPS[t[2]](t[1], t[3])

def p_number(t):
    '''
    NUMBER : FLOAT
           | INTEGER
    '''
    t[0] = t[1]

def p_expression_value(t):
    '''
    expression : NUMBER
               | TRUE
               | FALSE
               | NONE
    '''
    t[0] = t[1]

def p_expression_name(t):
    '''
    expression : NAME
    '''
    t[0] = names[t[1]]
    
def p_error(t):
    print "Syntax error at '%s'" % t.value

lexer = Lexer()
tokens = lexer.tokens
parser = yacc.yacc()

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        for line in open(sys.argv[1]):
            parser.parse(line, lexer=lexer)
    else:
        while True:
            try:
                s = raw_input('alex > ')
            except EOFError:
                print
                break
            except KeyboardInterrupt:
                print
                continue
            if not s:
                continue
            parser.parse(s, lexer = lexer)