#!/usr/bin/env python

from ply import yacc

from alexs_lang.lexer import Lexer
from alexs_lang import ast

class Parser(object):
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'UMINUS'),
        ('right', 'UPLUS'),
        ('left', 'POWER'),
    )

    def __init__(self):
        self._built = False
    
    def build(self, **kwargs):  
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)
    
    def parse(self, code):
        self.require_built()
        n = ast.NodeList()
        n.append(self.parser.parse(code, lexer=self.lexer))
        return n

    def require_built(self):
        if not self._built:
            self.build()
    
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
        if t[2] == '=':
            t[0] = ast.Assignment(ast.Name(t[1]), t[3])
        else:
            t[0] = ast.Assignment(ast.Name(t[1]), ast.BinaryOperation(ast.Name(t[1]), t[3], t[2][0]))

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
    
    def p_arglist(self, t):
        '''
        arglist : arglist COMMA expression
                | expression
        '''
        if len(t) == 2:
            t[0] = [t[1]]
        else:
            t[0] = t[1] + [t[3]]
    
    def p_expression_function_call(self, t):
        '''
        expression : expression LPAREN arglist RPAREN
        '''
        t[0] = ast.FunctionCall(t[1], t[3])
    
    def p_statement_if(self, t):
        '''
        statement : IF expression COLON suite
        '''
        t[0] = ast.If(t[2], t[4])

    def p_statements(self, t):
        '''
        statements : statements statement
                   | statement
        '''
        if len(t) == 2:
            t[0] = ast.NodeList([t[1]])
        else:
            t[1].append(t[2])
            t[0] = t[1]

    def p_suite(self, t):
        '''
        suite : NEWLINE INDENT statements DEDENT
        '''
        t[0] = t[3]

    def p_error(self, t):
        print "Syntax error at '%s'" % t.value
