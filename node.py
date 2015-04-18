
def printVar(var):
    '''
    Will return the printed version of var if it is a Node,
    otherwise will return var.
    :param var:
    :return:
    '''
    if isinstance(var,Node):
        var = var.print()
    return var

class Node:
    type = "NODE"
    def __init__(self,m = ""):
        self.msg = m    #used for error messages
    def print(self):
        return self.msg

#Not yet used!
########################
class Number(Node):
    type = "NUMBER"
    def __init__(self,n):
        self.num = n
    def print(self):
        return self.num
##########################

class String(Node):
    type = "STRING"
    def __init__(self,s):
        self.string = s
    def print(self):
        return self.string

class Transpose(Node):
    type="TRANSPOSE"
    def __init__(self,e):
        self.expr = printVar(e)
    def print(self):
        return self.expr+".T"

class Range(Node):
    def __init__(self,e1,e2,s=""):
        self.expr1 = printVar(e1)
        self.expr2 = printVar(e2)
        self.step = s
        if s is not "":
            self.step = ","+s
        if isinstance(e1,Range):
            self.expr1 = e1.expr1
            self.expr2 = e1.expr2
            self.step = ","+self.expr2
    def print(self):
        return "arange(%s,%s%s)"%(self.expr1,self.expr2,self.step)

class Expr(Node):
    type = "EXPR"
    def __init__(self,e1,op,e2):
        self.expr1 = printVar(e1)
        self.operator = op
        self.expr2 = printVar(e2)
    def print(self):
        return self.expr1+self.operator+self.expr2

class Bracket_Expr(Node):
    type = "BRACKET_EXPR"
    def __init__(self,e):
        self.expr = printVar(e)
    def print(self):
        return "("+self.expr+")"

class Stmt_List(Node):
    type = "STMT_LIST"
    def __init__(self,e1,e2):
        self.expr1 = e1
        self.expr2 = e2
    def print(self):
        return self.expr1.print()+"\n"+self.expr2.print()

class Global_List(Node):
    type = "GLOBAL_LIST"
    def __init__(self,i,g=None):
        self.iden = i
        self.glist = g
    def print(self):
        if self.glist is None:
            return self.iden
        else:
            return self.glist.print()+", "+self.iden

class Global_Stmt(Node):
    type = "GLOBAL_STMT"
    def __init__(self,i=None,e=None,g=None):
        self.glist = g
        self.iden = i
        self.expr = e
    def print(self):
        if self.glist is None:
            return "global "+self.ident+"="+self.expr.print()
        else :
            return "global "+self.glist.print()

class Loop(Node):
    pass

class For(Loop):
    type = "FOR"
    def __init__(self,i,e,s):
        self.item = i
        self.expr = e
        self.stmt = s
        self.expr.operator = ","
    def print(self):
        return "for %s in %s:"%(self.item,self.expr.print())+'\n'+self.stmt.print()

class If(Loop):
    type = "IF"
    def __init__(self,e,s,ef):
        self.expr = e
        self.stmt = s
        self.elseif = ef
    def print(self):
        return "if "+self.expr.print()+":\n"+self.stmt.print()+"\n"+self.elseif.print()

class ElseIf(Loop):
    type = "ELSE_IF"
    def __init__(self,e,s,ef):
        self.expr = e
        self.stmt = s
        self.elseif = ef
    def print(self):
        return "elif "+self.expr.print()+":\n"+self.stmt.print()+"\n"+self.elseif.print()

class Else(Loop):
    type = "ELSE"
    def __init__(self,s):
        self.stmt = s
    def print(self):
        return "else:\n"+self.stmt.print()

class Switch(Loop):
    type = "SWITCH"
    def __init__(self,e,cl):
        self.expr = e
        self.caselist = cl
    def print(self):
        return self.caselist.print(self.expr)

class Case_List(Loop):
    type = "CASE_LIST"
    def __init__(self,e=None,s=None,c=None,o=False):
        self.expr = printVar(e)
        self.stmtlist = s
        self.caselist = c
        self.otherwise = o
    def print(self,e,iselif=False):
        start = "if"
        if iselif:
            start = "elif"
        output = "%s %s == "%(start,e) +self.expr+":"
        if self.stmtlist is not None:
            output += "\n"+self.stmtlist.print()
        if self.caselist is not None:
            output+= "\n"+self.caselist.print(e,True)
        if self.otherwise:
            return "else:\n"+self.expr
        return output

class While(Loop):
    type = "WHILE"
    def __init__(self,e,s):
        self.expr = printVar(e)
        self.stmt = s
    def print(self):
        return "while %s:\n"%self.expr+self.stmt.print()



if __name__ == "__main__":
    ex = Expr("5",":","9")
    print(ex.print)
    t = For("i",ex)
    print (t.print())