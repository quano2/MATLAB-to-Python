import yacc as yacc
import Lexer

tokens = Lexer.tokens



def p_equals(p):
    ''' expr : EQUALS '''

def p_identifier(p):
    ''' expr : IDENTIFIER '''

def p_plus(p):
    ''' expr : expr PLUS term '''
    p[0] = p[1] + p[3]

def p_minus(p):
    ''' expr : expr MINUS term '''
    p[0] = p[1] - p[3]

def p_times(p):
    ''' expr : expr TIMES term '''
    p[0] = p[1] * p[3]

def p_div(p):
    ''' expr : expr DIV term '''
    p[0] = p[1] / p[3]

def p_and(p):
    ''' expr : AND '''
    p[0] = '&'

def p_plusplus(p):
    ''' expr : term PLUSPLUS term '''
    p[0] = p[1] + p[1]

def p_pluseequal(p):
    ''' expr : term PLUSEQUAL term '''
    p[0] = p[1] + p[1]

def p_subequal(p):
    ''' expr : term SUBEQUAL term '''
    p[0] = p[1] - p[1]

def p_timesequal(p):
    ''' expr : term TIMESEQUAL term '''
    p[0] = p[1] * p[1]

def p_divequal(p):
    ''' expr : term DIVEQUAL term '''
    p[0] = p[1] / p[3]

def p_equalto(p):
    ''' expr : expr EQUALTO term '''
    p[0] = p[1] == p[3]

def p_notequal(p):
    ''' expr : expr NOTEQUAL term '''
    p[0] = p[1] != p[3]

def p_lessthan(p):
    ''' expr : expr LESSTHAN term '''
    p[0] = p[1] < p[3]

def p_lessequal(p):
    ''' expr : expr LESSEQUAL term '''
    p[0] = p[1] <= p[3]

def p_greaterthan(p):
    ''' expr : expr GREATERTHAN term '''
    p[0] = p[1] > p[3]

def p_greaterequal(p):
    ''' expr : expr GREATEREQUAL term '''
    p[0] = p[1] >= p[3]

def p_not(p):
    ''' expr : NOT '''
    p[0] = '!'

def p_lbracket(p):
    ''' expr : LBRACKET '''
    p[0] = '('

def p_rbracket(p):
    ''' expr : RBRACKET '''
    p[0] = ')'

def p_lbrace(p):
    ''' expr : LBRACE '''
    p[0] = '{'

def p_rbrace(p):
    ''' expr : RBRACE '''
    p[0] = '}'

def p_number(p):
    ''' expr : NUMBER '''
    p[0] = p[1]

def p_string(p):
    ''' expr : STRING '''
    p[0] = p[1]

def p_transpose(p):
    ''' expr : TRANSPOSE '''
    p[0] = p[1]

def p_term(p):
    ''' term : NUMBER
             | IDENTIFIER
    '''

def p_error(p):
    print ('unable to parse %s' %p )

yacc.yacc()

data = "+"

output = yacc.parse(data)

print (output)