#!/usr/bin/env python

from ply import yacc

from alexs_lang.lexer import Lexer
from alexs_lang import ast

class Parser(object):
    precedence = (
        ('left', 'BIN_COMP'),
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
        self.parser = yacc.yacc(module=self, debug=2)
    
    def parse(self, code):
        self.require_built()
        return self.parser.parse(code, lexer=self.lexer)

    def require_built(self):
        if not self._built:
            self.build()

    def p_statement_list(self, t):
        '''
        statement_list : statement_list statement
                       | statement
        '''
        if len(t) == 2:
            t[0] = ast.NodeList([t[1]])
        else:
            t[1].append(t[2])
            t[0] = t[1]

    def p_statement(self, t):
        '''
        statement : assignment_statement NEWLINE
                  | expression NEWLINE
                  | if_statement
                  | def_statement
                  | return_statement NEWLINE
                  | for_statement
        '''
        t[0] = t[1]
    
    def p_assignable(self, t):
        '''
        assignable : name
                   | subscript
        '''
        t[0] = t[1]
    
    def p_name(self, t):
        '''
        name : NAME
        '''
        t[0] = ast.Name(t[1])
    
    def p_assignment_statement(self, t):
        '''
        assignment_statement : assignable EQUALS expression
                             | assignable PLUS_EQUALS expression
                             | assignable MINUS_EQUALS expression
                             | assignable TIMES_EQUALS expression
                             | assignable DIVIDE_EQUALS expression
        '''
        if t[2] == '=':
            t[0] = ast.Assignment([t[1]], t[3])
        else:
            t[0] = ast.Assignment([t[1]], ast.BinaryOperation(t[1], t[3], t[2][0]))

    def p_assignment_statement_multi(self, t):
        '''
        assignment_statement : assignable EQUALS assignment_statement
        '''
        t[0] = ast.Assignment([t[1]]+t[3].left, t[3].right)

    def p_expression_binary(self, t):
        '''
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
                   | expression MODULO expression
                   | expression POWER expression
                   | expression AND expression
                   | expression OR expression
                   | expression EQ expression %prec BIN_COMP
                   | expression LT expression %prec BIN_COMP
                   | expression GT expression %prec BIN_COMP
                   | expression LE expression %prec BIN_COMP
                   | expression GE expression %prec BIN_COMP
                   | expression NE expression %prec BIN_COMP
        '''
        t[0] = ast.BinaryOperation(t[1], t[3], t[2])

    def p_expression_unary(self, t):
        '''
        expression : MINUS expression %prec UMINUS
                   | PLUS expression %prec UPLUS
                   | NOT expression
        '''
        t[0] = ast.UnaryOperation(t[2], t[1])

    def p_expression_paren(self, t):
        '''
        expression : LPAREN expression RPAREN
        '''
        t[0] = t[2]

    def p_expression_const(self, t):
        '''
        expression : NUMBER
                   | BOOL
                   | none

        '''
        t[0] = t[1]

    def p_number(self, t):
        '''
        NUMBER : INTEGER
               | FLOAT
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
        expression : name
        '''
        t[0] = t[1]

    def p_arglist(self, t):
        '''
        arglist : arglist COMMA expression
                | expression
                |
        '''
        if len(t) == 2:
            t[0] = [t[1]]
        elif len(t) == 1:
            t[0] = []
        else:
            t[0] = t[1] + [t[3]]

    def p_functions(self, t):
        '''
        functions : name
        '''
        t[0] = t[1]

    def p_expression_function_call(self, t):
        '''
        expression : functions LPAREN arglist RPAREN
        '''
        t[0] = ast.FunctionCall(t[1], t[3])
    
    def p_if_statement(self, t):
        '''
        if_statement : IF expression COLON suite
        '''
        t[0] = ast.If(t[2], t[4])
    
    def p_if_statement_else(self, t):
        '''
        if_statement : IF expression COLON suite ELSE COLON suite
        '''
        t[0] = ast.If(t[2], t[4], t[7])
    
    def p_if_statement_elif(self, t):
        '''
        if_statement : IF expression COLON suite elif_statements
        '''
        t[0] = ast.If(t[2], t[4], None, t[5])
    
    def p_if_statements_elif_else(self, t):
        '''
        if_statement : IF expression COLON suite elif_statements ELSE COLON suite
        '''
        t[0] = ast.If(t[2], t[4], t[8], t[5])
    
    def p_elif_statements(self, t):
        '''
        elif_statements : elif_statements elif
                        | elif
        '''
        if len(t) == 2:
            t[0] = [t[1]]
        else:
            t[0] = t[1] + [t[2]]
    
    def p_elif(self, t):
        '''
        elif : ELIF expression COLON suite
        '''
        t[0] = (t[2], t[4])
    
    def p_def_statement(self, t):
        '''
        def_statement : DEF name LPAREN args RPAREN COLON suite
        '''
        t[0] = ast.Assignment([t[2]], ast.Function(t[4], t[7]))
    
    def p_args(self, t):
        '''
        args : args COMMA NAME
             | NAME
             |
        '''
        if len(t) == 2:
            t[0] = [t[1]]
        elif len(t) == 1:
            t[0] = []
        else:
            t[0] = t[1] + [t[3]]
    
    def p_return_statement(self, t):
        '''
        return_statement : RETURN expression
        '''
        t[0] = ast.Return(t[2])
    
    def p_for_statement(self, t):
        '''
        for_statement : FOR NAME IN expression COLON suite
        '''
        t[0] = ast.For(t[2], t[4], t[6])
    
    def p_expression_list(self, t):
        '''
        expression : LBRACKET arglist RBRACKET
        '''
        t[0] = ast.List(t[2])
    
    def p_expression_subscript(self, t):
        '''
        expression : subscript
        '''
        t[0] = t[1]
    
    def p_subscript(self, t):
        '''
        subscript : expression LBRACKET expression RBRACKET
        '''
        t[0] = ast.Subscript(t[1], t[3])
    
    def p_suite(self, t):
        '''
        suite : NEWLINE INDENT statement_list DEDENT
        '''
        t[0] = t[3]

    def p_error(self, t):
        import sys
        sys.stderr.write("Syntax error at '%s' on line %s.\n" % (t.value, t.lineno))
