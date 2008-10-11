#!/usr/bin/env python

from ply import yacc

from alexs_lang.lexer import Lexer
from alexs_lang import ast

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
    ('left', 'POWER'),
)

class Parser(object):
    def build(self, **kwargs):
        self.lexer = Lexer()
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(object=self)
    
    def parse(self, code):
        n = ast.NodeList()
        for line in code:
            n.append(self.parser.parse(line, lexer=self.lexer))
        return n
    
    def p_statement(self, t):
        '''
        statement : statement NEWLINE
        '''
        t[0] = t[1]

    def p_statement_expr(self, t):
        '''
        statement : expression
        '''
        t[0] = t[1]

    def p_expression(self, t):
        '''
        expression : NAME EQUALS expression
                   | NAME PLUS_EQUALS expression
                   | NAME MINUS_EQUALS expression
                   | NAME TIMES_EQUALS expression
                   | NAME DIVIDE_EQUALS expression
        '''
        t[0] = ast.Assignment(ast.Name(t[1]), t[3], t[2])

    def p_expression_binop(self, t):
        '''
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
                   | expression MODULO expression
                   | expression POWER expression
        '''
        t[0] = ast.BinaryOperation(t[1], t[3], t[2])

    def p_expression_unaryop(self, t):
        '''
        expression : MINUS expression %prec UMINUS
                   | PLUS expression %prec UPLUS
                   | NOT expression
        '''
        t[0] = ast.UnaryOperation(t[2], t[1])

    def p_expression_group(self, t):
        '''
        expression : LPAREN expression RPAREN
        '''
        t[0] = t[2]

    def p_expression_compare(self, t):
        '''
        expression : expression EQ expression
                   | expression LT expression
                   | expression GT expression
                   | expression LE expression
                   | expression GE expression
                   | expression AND expression
                   | expression OR expression
        '''
        t[0] = ast.Comparison(t[1], t[3], t[2])

    def p_expression_constant(self, t):
        '''
        expression : NUMBER
                   | BOOL
                   | none
        '''
        t[0] = t[1]

    def p_number(self, t):
        '''
        NUMBER : FLOAT
               | INTEGER
        '''
        t[0] = ast.Number(t[1])

    def p_bool(self, t):
        '''
        BOOL : TRUE
             | FALSE
        '''
        t[0] = ast.Boolean(t[1])

    def p_none(self, t):
        '''
        none : NONE
        '''
        t[0] = ast.NoneVal()

    def p_expression_name(self, t):
        '''
        expression : NAME
        '''
        t[0] = ast.Name(t[1])

    def p_error(self, t):
        print "Syntax error at '%s'" % t.value
