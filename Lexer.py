#This is the lexer file which is still incomplete
#version - 1

__author__ = 'Joe'
import lex

class UnknownCharacterError(Exception):
    pass


#Tokens

tokens = [
    'EQUALS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LDIV',
    'AND',
    'ANDAND',
    'EQUALEQUAL',
    'NOTEQUAL',
    'LESSTHAN',
    'LESSEQUAL',
    'GREATERTHAN',
    'GREATEREQUAL',
    'NUMBER',
    'STRING',
    'TRANSPOSE',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'IDENTIFIER',
    'SEMI',
    'COLON',
    'COMMA',
    'FIELD',
    'OR',
    'OREQUALS',
    'OROR',
    'DOT',
    'DOTDIV',
    'DOTEXP',
    'DOTMUL',
    'EXP',
    'NOT'

]

#Keywords

reserved = {
    'break'     : 'BREAK',
    'case'      : 'CASE',
    'else'      : 'ELSE',
    'elseif'    : 'ELSEIF',
    'end'       : 'END',
    'for'       : 'FOR',
    'if'        : 'IF',
    'otherwise' : 'OTHERWISE',
    'return'    : 'RETURN',
    'switch'    : 'SWITCH',
    'while'     : 'WHILE',
    'continue'  : 'CONTINUE',
    'try'       : 'TRY',
    'catch'     : 'CATCH',
    'global'    : 'GLOBAL',
    'function'  : 'FUNCTION'
}
tokens += list(reserved.values())

def new():
    comments = []

    t_EQUALS        = r'\='
    t_PLUS          = r'\+'
    t_MINUS         = r'-'
    t_TIMES         = r'\*'
    t_DIV           = r'/'
    t_LDIV          = r'\\'
    t_AND           = r'\&'
    t_ANDAND        = r'\&\&'
    t_EQUALEQUAL    = r'\=='
    t_NOTEQUAL      = r'\~='
    t_LESSTHAN      = r'\<'
    t_LESSEQUAL     = r'\<='
    t_GREATERTHAN   = r'\>'
    t_GREATEREQUAL  = r'\>='
    t_LBRACKET      = r'\('
    t_RBRACKET      = r'\)'
    t_LBRACE        = r'\{'
    t_RBRACE        = r'\}'
    t_SEMI          = r'\;'
    t_COLON         = r'\:'
    t_OR            = r'\|'
    t_OREQUALS      = r'\|='
    t_OROR          = r'\|\|'
    t_DOT           = r'\.'
    t_DOTDIV        = r"\./"
    t_DOTEXP        = r"\.\^"
    t_DOTMUL        = r"\.\*"
    t_EXP           = r"\^"
    t_NOT           = r"\~"

    def t_NUMBER(t):
        r"(0x[0-9A-Fa-f]+)|((\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?[ij]?)"
        t.value = float(t.value)
        return t

    def t_STRING(t):
        r"\'[a-zA-Z][a-zA-z0-9]*\'"
        return t

    def t_TRANSPOSE(t):
        r"([\.]?\')"
        return t

    def t_IDENTIFIER(t):
        r"\.?[a-zA-Z_]+[a-zA-Z0-9_]*"
        if t.value[0] == ".":
            t.type = "FIELD"
            return t
        elif t.value=="persistent":
            pass    #ignore persistent no use in python
        elif t.value in reserved:
            t.type = reserved.get(t.value,'ID')
            return t
        else:
            return t

    def t_COMMA(t):
        r","
        print (t.lexer.lineno)
        return t

    def t_comment(t):
        r"%.*"
        temp = list(t.value)
        temp.pop(0)
        t.value = "".join(temp)     #removes % sign from comment
        comments.append((t.value,lexer.lineno))

    def t_error(t):
        raise UnknownCharacterError(t.value[0],t.lineno)

    def t_SPACES(t):
        r"[ |\t]"
        pass

    def t_newline(t):
        r"\n"
        t.lexer.lineno += 1
        t.type= "SEMI"
        t.value=";"
        #return t    commented out so it will work with code over lines.

    lexer = lex.lex()
    lexer.comments = comments
    return lexer

if __name__ == '__main__':
    lexer = new()
    data =  '''p= 'hello'.';
    t'
    t.'
            '''

    lexer.input(data)

    for tok in lexer:
        print(tok)
    if lexer.comments:
        print(lexer.comments)