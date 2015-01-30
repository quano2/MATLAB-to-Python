#This is the lexer file which is still incomplete
#version - 1

__author__ = 'Joe'
import lex

#Tokens

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'AND',
    'PLUSPLUS',
    'PLUSEQUAL',
    'SUBEQUAL',
    'TIMESEQUAL',
    'DIVEQUAL',
    'EQUALTO',
    'NOTEQUAL',
    'LESSTHAN',
    'LESSEQUAL',
    'GREATERTHAN',
    'GREATEREQUAL',
    'NOT',
    'NUMBER',
    'STRING',
    'TRANSPOSE',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'ADD'
)

#Keywords

reserved = {
    'break'     : 'BREAK',
    'case'      : 'CASE',
    'else'      : 'ELSE',
    'elseif'    : 'ELSEIF',
    'end'       : 'END',
    'error'     : 'ERROR',
    'for'       : 'FOR',
    'if'        : 'IF',
    'otherwise' : 'OTHERWISE',
    'return'    : 'RETURN',
    'switch'    : 'SWITCH',
    'warning'   : 'WARNING',
    'while'     : 'WHILE',
    'continue'  : 'CONTINUE',
    'try'       : 'TRY',
    'catch'     : 'CATCH'
}

t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIV           = r'/'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_ADD           = r'\&'
t_PLUSPLUS      = r'\+\+'
t_PLUSEQUAL     = r'\+='
t_SUBEQUAL      = r'\-='
t_TIMESEQUAL    = r'\*='
t_DIVEQUAL     = r'\/='
t_EQUALTO       = r'\=='
t_NOTEQUAL      = r'\!='
t_LESSTHAN      = r'\<'
t_LESSEQUAL     = r'\<='
t_GREATERTHAN   = r'\>'
t_GREATEREQUAL  = r'\>='
t_NOT           = r'\!'
t_LBRACKET      = r'\('
t_RBRACKET      = r'\)'
t_LBRACE        = r'\{'
t_RBRACE        = r'\}'

def t_NUMBER(t):
    r'(^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'^[a-zA-Z][a-zA-z0-9]*'
    return t

def t_TRANSPOSE(t):
    r'\t'
    return t

def t_error(t):
    print("Invalid character: '%s' " %t.value)
    t.lexer.skip(1)



if __name__ == '__main__':
    print(tokens)
    print("There are " , len(tokens),  " Tokens")
    print(reserved.keys())
    print("There are ", len(reserved), " Keywords")
    lexer = lex.lex()
    data = "6 + 9"

    lexer.input(data)

    for tok in lexer:
        print(tok)