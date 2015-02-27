#This is the lexer file which is still incomplete
#version - 1

__author__ = 'Joe'
import lex

#Tokens

tokens = (
    'EQUALS',
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
    'IDENTIFIER'
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

t_EQUALS        = r'\='
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIV           = r'/'
t_AND           = r'\&'
t_PLUSPLUS      = r'\+\+'
t_PLUSEQUAL     = r'\+='
t_SUBEQUAL      = r'\-='
t_TIMESEQUAL    = r'\*='
t_DIVEQUAL      = r'\/='
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
    r"(0x[0-9A-Fa-f]+)|((\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?[ij]?)"

    t.value = float(t.value)
    return t

def t_STRING(t):
    r"^[a-zA-Z][a-zA-z0-9]*"   #Add search for '
    return t

def t_TRANSPOSE(t):
    r"[\w]+\.'"
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_]+[a-zA-Z0-9_]*"
    return t

def t_error(t):
    print("Invalid character: '%s' " %t.value)
    t.lexer.skip(1)

def t_comment(t):
    r"%.*"
    pass

def t_SPACES(t):
    r"[ |\t]"
    pass

def t_newline(t):
    r"\n"
    t.lexer.lineno += t.value.count('/n')

lexer = lex.lex()

if __name__ == '__main__':
    lexer = lex.lex()
    data = "5"

    lexer.input(data)

    for tok in lexer:
        print(tok)