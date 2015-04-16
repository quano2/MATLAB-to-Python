
class Node:
    type = "NODE"
    def __init__(self,m = ""):
        self.tabs=0
        self.msg = m
    def print(self):
        return self.msg

class Expr(Node):
    type = "EXPR"
    def __init__(self,e1,op,e2):
        self.expr1 = e1
        self.operator = op
        self.expr2 = e2
    def print(self):
        if isinstance(self.expr1,Node):
            self.expr1 = self.expr1.print()
        if isinstance(self.expr2,Node):
            self.expr2 = self.expr2.print()
        return self.tab()+self.expr1+self.operator+self.expr2

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
        return "for %s in range(%s):"%(self.item,self.expr.print())+'\n'+self.stmt.print()


class Stmt_List(Node):
    type = "STMT_LIST"
    def __init__(self,e1,e2):
        self.expr1 = e1
        self.expr2 = e2
    def print(self):
        return self.expr1.print()+"\n"++self.expr2.print()


if __name__ == "__main__":
    ex = Expr("5",":","9")
    print(ex.print)
    t = For("i",ex)
    print (t.print())