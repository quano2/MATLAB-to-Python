import yacc as yacc
import Lexer
from Lexer import tokens
from node import *

class MySystemError(Exception):
    pass
class NotSupported(Exception):
    pass
class UnknownError(Exception):
    pass

precedence = (
    ("right","EQUALS","OREQUALS"),
    ("left", "COMMA"),
    ("left", "COLON"),
    ("left", "OROR","ANDAND"),
    ("left", "EQUALEQUAL", "NOTEQUAL", "GREATEREQUAL", "LESSEQUAL", "GREATERTHAN", "LESSTHAN"),
    ("left", "OR", "AND"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES","DIV","DOTMUL","DOTDIV","LDIV"),
    ("right","UMINUS","NOT"),
    ("right","TRANSPOSE"),
    ("right","EXP", "DOTEXP"),
    ("nonassoc","RBRACE","LBRACE"),
    ("left", "FIELD","DOT")
)

global indentlist
global counter
global start
start = 0
counter =0
indentlist = []

def indent(start,end):
    global indentlist
    indentlist.append([start,end])

def p_top(p):
    """
    top :
        | stmt_list
        | top func_decl stmt_list_opt
        | top func_decl end semi_opt
        | top func_decl stmt_list end semi_opt
    """
    print("top")
    if len(p)==2:
        p[0] = p[1]
    else:
        print ("Different")

def p_semi_opt(p):
    """
    semi_opt :
             | semi_opt SEMI
             | semi_opt COMMA
    """
    print("semi_opt")
    pass

def p_stmt(p):
    """
    stmt    : continue_stmt
            | break_stmt
            | expr_stmt
            | global_stmt
            | command
            | for_stmt
            | if_stmt
            | null_stmt
            | return_stmt
            | switch_stmt
            | try_catch
            | while_stmt
    """
    print("stmt")
    #| foo_stmt missing
    p[0] = p[1]


def p_arg1(p):
    """
    arg1    : STRING
            | NUMBER
            | IDENTIFIER
            | GLOBAL
    """
    print("arg1")
    p[0] = p[1]
        #not sure what this is here for??


def p_args(p):
    """
    args    : arg1
            | args arg1
    """
    print("arg")
    if len(p)==2:
        p[0]=p[1]
    else:
        p[0]=p[1],p[2]
        #not sure what this is here for??

def p_command(p):
    """
    command : IDENTIFIER args SEMI
    """
    print("command")
    #not sure what this is here for??
    raise NotSupported("Command",p.lineno(1))

def p_global_list(p):
    """global_list  : IDENTIFIER
                    | global_list IDENTIFIER
    """
    print("global_list")
    if len(p)==2:
        p[0] = Global_List(p[1])
    else:
        p[0] = Global_List(p[2],p[1])

def p_global_stmt(p):
    """
    global_stmt : GLOBAL global_list SEMI
                | GLOBAL IDENTIFIER EQUALS expr SEMI
    """
    print("global_stmt")
    if len(p)==4:
        p[0] = Global_Stmt(g= p[2])
    else:
        p[0] = Global_Stmt(i=p[2],e=p[4])
#def p_foo_stmt(p):
#    """
#    foo_stmt : expr OROR expr SEMI
#    """


def p_return_stmt(p):
    """
    return_stmt : RETURN SEMI
    """
    print("return_stmt")
    p[0] = String(p[1])

def p_continue_stmt(p):
    """
    continue_stmt : CONTINUE SEMI
    """
    print("continue_stmt")
    p[0] = String(p[1])

def p_break_stmt(p):
    """
    break_stmt : BREAK SEMI
    """
    print("break_stmt")
    p[0] = String(p[1])

def p_switch_stmt(p):
    """
    switch_stmt : SWITCH expr semi_opt case_list end
    """
    print("switch_stmt")
    p[0] = Switch(p[2],p[4])

def p_case_list(p):
    """
    case_list   :
                | CASE expr sep stmt_list_opt case_list
                | CASE expr error stmt_list_opt case_list
                | OTHERWISE stmt_list
    """
    print("case_list")
    if len(p)==1:
        pass
    elif len(p)==3: # Otherwise
        p[0] = Case_List(e=p[2],o=True)
        global start
        start = p.lineno(1)
    else:
        p[0] = Case_List(e=p[2],s=p[4],c=p[5])
        indent(p.lineno(2),p.lineno(5)-1-counter)

def p_try_catch(p):
    """
    try_catch   : TRY stmt_list CATCH stmt_list end
                | TRY stmt_list end
    """
    print("try_catch")
    if len(p)==4:
        p[0] = (p[1],p[2],p[3])
    else:
        p[0] = (p[1],p[2],p[3],p[4])

def p_null_stmt(p):
    """
    null_stmt   : SEMI
                | COMMA
    """
    print("null_stmt")
    global counter
    counter +=1
    pass

def p_func_decl(p):
    """func_decl    : FUNCTION IDENTIFIER args_opt SEMI
                    | FUNCTION ret EQUALS IDENTIFIER args_opt SEMI
    """
    print("func_decl")
    if len(p)==5:
        p[0] = (p[1],p[2],p[3])
    else:
        p[0] = (p[1],p[2],p[3],p[4],p[5])

def p_args_opt(p):
    """
    args_opt    :
                | LBRACKET RBRACKET
                | LBRACKET expr_list RBRACKET
    """
    print("args_opt")
    if len(p)==1:
        p[0] = ''  #empty for now
    elif len(p)==2:
        p[0] = (p[1],"",p[2])
    else:
        p[0] = (p[1],p[2],p[3])

#def p_arg_list(p):
#    """
#    arg_list    : IDENTIFIER
#                | arg_list COMMA IDENTIFIER
#    """
#    print("arg_list")
#Not sure if needed or not, not used so unreachable

def p_ret(p):
    """
    ret : IDENTIFIER
        | LBRACKET RBRACKET
        | LBRACKET expr_list RBRACKET
    """
    print("ret")
    if len(p)==2:
        p[0] = p[1]
    elif len(p)==3:
        p[0] = (p[1],"",p[2])
    else:
        p[0] = (p[1],p[2],p[3])

def p_stmt_list_opt(p):
    """
    stmt_list_opt   :
                    | stmt_list
    """
    print("stmt_list_opt")
    if len(p)==1:
        p[0] = ""     #This is wrong!!!
        raise NotSupported("stmt_list_opt",p.lineno(0))
    else:
        p[0] = p[1]

def p_stmt_list(p):
    """
    stmt_list   : stmt
                | stmt_list stmt
    """
    print("stmt_list")
    if len(p)==2:
        p[0] = p[1]
    else:
        if p[2]==None:  #ignore ; between lines, might be wrong
            p[0]=p[1]
        elif p[1]==None or p[1]=="ERROR": #might be wrong, but removes Nones and ERROR
            p[0] = p[2]
        else:
            p[0] = Stmt_List(p[1],p[2])

def p_concat_list(p):
    """
    concat_list : expr_list SEMI expr_list
                | concat_list SEMI expr_list
    """
    print("concat_list + FIX")
    p[0]= (p[1],p[3])    #no idea

def p_expr_list(p):
    """
    expr_list   : exprs
                | exprs COMMA
    """
    print("expr_list")
    p[0] = p[1]

def p_exprs(p):
    """
    exprs   : expr
            | exprs COMMA expr
    """
    print("exprs")
    if len(p)==2:
        p[0]=(p[1])
    else:
        p[0] = (p[1],p[2],p[3]) #guess

def p_expr_stmt(p):
    """
    expr_stmt : expr_list SEMI
    """
    print("expr_stmt")
    p[0] = p[1]

def p_while_stmt(p):
    """
    while_stmt : WHILE expr SEMI stmt_list end
    """
    print("while_stmt")
    indent(p.lineno(1)+1,p.lineno(5)-counter)
    p[0] = While(p[2],p[4])

def p_separator(p):
    """
    sep     : COMMA
            | SEMI
    """
    print("separator")
    p[0]=p[1]

def p_if_stmt(p):
    """
    if_stmt : IF expr sep stmt_list_opt elseif_stmt end
            | IF expr error stmt_list_opt elseif_stmt end
    """
    print("if_stmt")
    indent(p.lineno(1)+1,p.lineno(5)-counter)
    p[0] = If(p[2],p[4],p[5])

def p_elseif_stmt(p):
    """
    elseif_stmt :
                | ELSE stmt_list_opt
                | ELSEIF expr sep stmt_list_opt elseif_stmt
    """
    print("elseif_stmt")
    if len(p)==1:
        p[0] = Node()
    elif len(p)==3:
        indent(p.lineno(1),p.lineno(2)-counter+1)
        p[0] = Else(p[2])
        print ("ELIF",p.lineno(1)+1,p.lineno(2)-counter)

    else:
        indent(p.lineno(1),p.lineno(4)-counter)
        p[0] = ElseIf(p[2],p[4],p[5])
        print ("ELSE",p.lineno(1)+1,p.lineno(4)-counter)

def p_for_stmt(p):
    """
    for_stmt    : FOR IDENTIFIER EQUALS expr SEMI stmt_list end
                | FOR LBRACKET IDENTIFIER EQUALS expr RBRACKET SEMI stmt_list end
                | FOR matrix EQUALS expr SEMI stmt_list end
    """
    print("for_stmt")
    indent(p.lineno(1)+1,p.lineno(7)-counter)
    if len(p)==8:
        print("whatis this",p[4])
        if not isinstance(p[4],Range):
           raise MySystemError(p.lineno(4),p[4].operator)
        p[0] = For(p[2],p[4],p[6])
    elif len(p)==10:
        raise NotSupported("Unknown",p.lineno(4))
    else:
        raise NotSupported("Matrix for loop",p.lineno(4))

def p_expr_number(p):
    """
    number : NUMBER
    """
    p[0] = p[1]

def p_expr(p):
    """expr : IDENTIFIER
            | number
            | string
            | colon
            | NOTEQUAL
            | NOT
            | matrix
            | cellarray
            | expr2
            | expr1
    """
    print("expr")
    p[0] = p[1]

def p_expr_end(p):
    """
    end : END
    """
    print("expr_end")
    global counter, start
    counter +=1
    if start != 0:
        indent(start,p.lineno(1)-counter)
        start = 0
    p[0] = p[1]

def p_expr_string(p):
    """
    string : STRING
    """
    print("expr_string")
    p[0] = String(p[1])

def p_expr_colon(p):
    """
    colon : COLON
    """
    print("expr_colon")
    p[0] = String(p[1])

def p_expr1(p):
    """expr1    : MINUS expr %prec UMINUS
                | PLUS expr %prec UMINUS
                | NOTEQUAL expr
    """
    print("expr1")
    p[0] = Expr(p[1],"",p[2])

def p_cellarray(p):
    """
    cellarray   : LBRACE RBRACE
                | LBRACE expr_list RBRACE
                | LBRACE concat_list RBRACE
                | LBRACE concat_list SEMI RBRACE
    """
    print("cellarray")
    raise NotSupported("Cell array",p.lineno(1))
    # Cell arrays will not be supported.

def p_matrix(p):
    """matrix   : LBRACKET RBRACKET
                | LBRACKET concat_list RBRACKET
                | LBRACKET concat_list SEMI RBRACKET
                | LBRACKET expr_list RBRACKET
                | LBRACKET expr_list SEMI RBRACKET
    """
    print("matrix")
    raise NotSupported("Matrix",p.lineno(1))
    # Matrices are not supported currently

def p_paren_expr(p):
    """
    expr : LBRACKET expr RBRACKET
    """
    print("paren_expr")
    p[0]=Bracket_Expr(p[2])

def p_field_expr(p):
    """
    expr : expr FIELD
    """
    print("field_expr")
    p[0] = (p[2],p[1])
    #no idea what this is

def p_transpose_expr(p):
# p[2] contains the exact combination of plain and conjugate
# transpose operators, such as "'.''.''''".
    """
    expr : expr TRANSPOSE
    """
    print("transpose_expr")
    p[0] = Transpose(p[1])

def p_cellarrayref(p):
    """expr : expr LBRACE expr_list RBRACE
            | expr LBRACE RBRACE
    """
    print("cellarrayref")
    # Not supported
    raise NotSupported("Cell array reference",p.lineno(4))

def p_funcall_expr(p):
    """expr : expr LBRACKET expr_list RBRACKET
            | expr LBRACKET RBRACKET
    """
    print("funcall_expr")
    #LOOK THIS UP IN GRAMMAR!!!!
    raise NotSupported("funcall_expr",p.lineno(4))

def p_expr2(p):
    """expr2    : expr AND expr
                | expr ANDAND expr
                | expr LDIV expr
                | expr COLON expr
                | expr DIV expr
                | expr DOT expr
                | expr DOTDIV expr
                | expr DOTEXP expr
                | expr DOTMUL expr
                | expr EQUALEQUAL expr
                | expr EXP expr
                | expr GREATEREQUAL expr
                | expr GREATERTHAN expr
                | expr LESSEQUAL expr
                | expr LESSTHAN expr
                | expr MINUS expr
                | expr TIMES expr
                | expr NOTEQUAL expr
                | expr OR expr
                | expr OROR expr
                | expr PLUS expr
                | expr EQUALS expr
                | expr OREQUALS expr
    """
    print("expr2")
    print("check here!!!",p[2])
    if len(p)==6:
        p[0] = Range(p[1],p[3],p[5])
    elif p[2]==":":
        p[0] = Range(p[1],p[3])
    else:
        p[0]=Expr(p[1],p[2],p[3])
# The algorithm, which decides if an
# expression F(X)
# is arrayref or funcall, is implemented in
# resolve.py, except the following lines up
# to XXX. These lines handle the case where
# an undefined array is updated:
# >>> clear a
# >>> a[1:10]=123
# Though legal in matlab, these lines
# confuse the algorithm, which thinks that
# the undefined variable is a function name.
# To prevent the confusion, we mark these
# nodes arrayref as early as during the parse
# phase.

def p_error(p):
    print ('unable to parse %s' %p )
    if p is not None:
        raise MySystemError(p.lineno,p.value)
    else:
        raise UnknownError(p)

def myparser(input,debug=0):
    mylexer = Lexer.new()
    yacc.yacc()
    try:
        output = yacc.parse(input,lexer=mylexer,tracking=True,debug=debug)
        return output,indentlist
    except Lexer.UnknownCharacterError as e:
        return Node("An Invalid character '%s' has been found on line '%s'"%e.args)
    except MySystemError as e:
        return Node("Syntax error on line '%s' at '%s'"%e.args)
    except NotSupported as e:
        return Node ("Parser detected a '%s' on line '%s' which is not supported."%e.args)
    except UnknownError:
        return Node ("Parser has come across a syntax error, please check for ';' at line ends.")


if __name__ == "__main__":
    nlex = Lexer.new()
    yacc.yacc()

    data =  """i = 5 + 5;
"""

    #output = yacc.parse(data,lexer=nlex,debug=1)
    output = myparser(data)
    print ()
    print (output)
    #print (Lexer.comments)