import yacc as yacc
import Lexer

tokens = Lexer.tokens
precedence = (
    ("nonassoc", "LESSTHAN", "LESSEQUAL", "GREATERTHAN", "GREATEREQUAL"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES","DIV"),
    ("right","TRANSPOSE"),
    ("left","PLUSPLUS","MINUSMINUS"),
    ("right","UMINUS")
)

def p_top(p):
    """
    top :
        | stmt_list
        | top func_decl stmt_list_opt
        | top func_decl end semi_opt
        | top func_decl stmt_list end semi_opt
    """

def p_semi_opt(p):
    """
    semi_opt :
             | semi_opt SEMI
             | semi_opt COMMA
    """
    pass

def p_stmt(p):
    """
    stmt    : continue_stmt
            | break_stmt
            | expr_stmt
            | global_stmt
            | persistent_stmt
            | command
            | for_stmt
            | if_stmt
            | null_stmt
            | return_stmt
            | switch_stmt
            | try_catch
            | while_stmt
            | foo_stmt
    """
    p[0] = p[1]

def p_arg1(p):
    """
    arg1    : STRING
            | NUMBER
            | IDENTIFIER
            | GLOBAL
    """

def p_args(p):
    """
    args    : arg1
            | args arg1
    """
def p_command(p):
    """
    command : IDENTIFIER args SEMI
    """

def p_global_list(p):
    """global_list  : IDENTIFIER
                    | global_list IDENTIFIER
    """

def p_global_stmt(p):
    """
    global_stmt : GLOBAL global_list SEMI
                | GLOBAL IDENTIFIER EQUALS expr SEMI
    """

def p_foo_stmt(p):
    "foo_stmt : expr OROR expr SEMI"

def p_persistent_stmt(p):
    """
    persistent_stmt : PERSISTENT global_list SEMI
    | PERSISTENT IDENTIFIER EQUALS expr SEMI
    """

def p_return_stmt(p):
    "return_stmt : RETURN SEMI"

def p_continue_stmt(p):
    "continue_stmt : CONTINUE SEMI"

def p_break_stmt(p):
    "break_stmt : BREAK SEMI"

def p_switch_stmt(p):
    """
    switch_stmt : SWITCH expr semi_opt case_list end
    """

def p_case_list(p):
    """
    case_list   :
                | CASE expr sep stmt_list_opt case_list
                | CASE expr error stmt_list_opt case_list
                | OTHERWISE stmt_list
    """

def p_try_catch(p):
    """
    try_catch   : TRY stmt_list CATCH stmt_list end
                | TRY stmt_list end
    """

def p_null_stmt(p):
    """
    null_stmt   : SEMI
                | COMMA
    """
    p[0] = None

def p_func_decl(p):
    """func_decl    : FUNCTION IDENTIFIER args_opt SEMI
                    | FUNCTION ret EQUALS IDENTIFIER args_opt SEMI
    """

def p_args_opt(p):
    """
    args_opt    :
                | LBRACKET RBRACKET
                | LBRACKET expr_list RBRACKET
    """

def p_arg_list(p):
    """
    arg_list    : IDENTIFIER
                | arg_list COMMA IDENTIFIER
    """

def p_ret(p):
    """
    ret : IDENTIFIER
        | LBRACKET RBRACKET
        | LBRACKET expr_list RBRACKET
    """

def p_stmt_list_opt(p):
    """
    stmt_list_opt   :
                    | stmt_list
    """

def p_stmt_list(p):
    """
    stmt_list   : stmt
                | stmt_list stmt
    """

def p_concat_list(p):
    """
    concat_list : expr_list SEMI expr_list
                | concat_list SEMI expr_list
    """

def p_expr_list(p):
    """
    expr_list   : exprs
                | exprs COMMA
    """

def p_exprs(p):
    """
    exprs   : expr
            | exprs COMMA expr
    """

def p_expr_stmt(p):
    """
    expr_stmt : expr_list SEMI
    """

def p_while_stmt(p):
    """
    while_stmt : WHILE expr SEMI stmt_list end
    """

def p_separator(p):
    """
    sep     : COMMA
            | SEMI
    """

def p_if_stmt(p):
    """
    if_stmt : IF expr sep stmt_list_opt elseif_stmt end
            | IF expr error stmt_list_opt elseif_stmt end
    """

def p_elseif_stmt(p):
    """
    elseif_stmt :
                | ELSE stmt_list_opt
                | ELSEIF expr sep stmt_list_opt elseif_stmt
    """

def p_for_stmt(p):
    """
    for_stmt    : FOR IDENTIFIER EQUALS expr SEMI stmt_list end
                | FOR LBRACKET IDENTIFIER EQUALS expr RBRACKET SEMI stmt_list end
                | FOR matrix EQUALS expr SEMI stmt_list end
    """

def p_expr(p):
    """expr : IDENTIFIER
            | end
            | number
            | string
            | colon
            | NOTEQUAL
            | matrix
            | cellarray
            | expr2
            | expr1
            | expr PLUSPLUS
            | expr MINUSMINUS
    """


def p_lambda_args(p):
    """lambda_args  : LBRACKET RBRACKET
                    | LBRACKET arg_list RBRACKET
    """

def p_expr_number(p):
    "number : NUMBER"

def p_expr_end(p):
    "end : END"

def p_expr_string(p):
    "string : STRING"

def p_expr_colon(p):
    "colon : COLON"

def p_expr1(p):
    """expr1    : MINUS expr %prec UMINUS
                | PLUS expr %prec UMINUS
                | NOTEQUAL expr
                | PLUSPLUS IDENTIFIER
                | MINUSMINUS IDENTIFIER
    """

def p_cellarray(p):
    """
    cellarray   : LBRACE RBRACE
                | LBRACE expr_list RBRACE
                | LBRACE concat_list RBRACE
                | LBRACE concat_list SEMI RBRACE
    """

def p_matrix(p):
    """matrix   : LBRACKET RBRACKET
                | LBRACKET concat_list RBRACKET
                | LBRACKET concat_list SEMI RBRACKET
                | LBRACKET expr_list RBRACKET
                | LBRACKET expr_list SEMI RBRACKET
    """

def p_paren_expr(p):
    """
    expr : LBRACKET expr RBRACKET
    """
def p_field_expr(p):
    """
    expr : expr FIELD
    """

def p_transpose_expr(p):
# p[2] contains the exact combination of plain and conjugate
# transpose operators, such as "'.''.''''".
    "expr : expr TRANSPOSE"

def p_cellarrayref(p):
    """expr : expr LBRACE expr_list RBRACE
            | expr LBRACE RBRACE
    """

def p_funcall_expr(p):
    """expr : expr LBRACKET expr_list RBRACKET
            | expr LBRACKET RBRACKET
    """

def p_expr2(p):
    """expr2    : expr AND expr
                | expr LDIV expr
                | expr COLON expr
                | expr DIV expr
                | expr DOT expr
                | expr DOTDIV expr
                | expr DOTDIVEQUALS expr
                | expr DOTEXP expr
                | expr DOTMUL expr
                | expr DOTMULEQUALS expr
                | expr EQUALSEQUALS expr
                | expr EXP expr
                | expr EXPEQUALS expr
                | expr GE expr
                | expr GT expr
                | expr LE expr
                | expr LT expr
                | expr MINUS expr
                | expr MUL expr
                | expr NE expr
                | expr OR expr
                | expr OROR expr
                | expr PLUS expr
                | expr EQUALS expr
                | expr MULEQUALS expr
                | expr DIVEQUALS expr
                | expr MINUSEQUALS expr
                | expr PLUSEQUALS expr
                | expr OREQUALS expr
                | expr ANDEQUALS expr
    """
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

yacc.yacc()

data = "i * 5 *4"

output = yacc.parse(data)

print (output)