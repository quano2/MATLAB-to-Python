import yacc as yacc
import Lexer

tokens = Lexer.tokens


def p_expr(p):
    '''expr : EQUALS
            | PLUS
            | MINUS
            | TIMES
            | DIV
            | AND
            | PLUSPLUS
            | PLUSEQUAL
            | SUBEQUAL
            | TIMESEQUAL
            | DIVEQUAL
            | EQUALTO
            | NOTEQUAL
            | LESSTHAN
            | LESSEQUAL
            | GREATERTHAN
            | GREATEREQUAL
            | NOT
            | LBRACKET
            | RBRACKET
            | LBRACE
            | RBRACE
            | term
    '''
    p[0] = p[1]
    print ('EXPR',p[0])
def p_term(p):
    ''' term : NUMBER
             | IDENTIFIER
             | STRING
    '''
    p[0] = p[1]

#def p_expr_number(p):
#    ''' number : NUMBER
#    '''
#9    p[0] = str(p[1])

def p_transpose(p):
    ''' expr : TRANSPOSE
    '''
    return p[0]

def p_error(p):
    print ('unable to parse %s' %p )

yacc.yacc()

data = "5"

output = yacc.parse(data)

print (output)