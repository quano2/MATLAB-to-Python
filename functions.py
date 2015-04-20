functions={
#   MATLAB  :   PYTHON
    "eps"       :   "spacing(1)",
    "ndims"     :   "ndim",
    "size"      :   "shape",
    "find"      :   "nonzero",
    "rand"      :   "random.rand",
    "repmat"    :   "tile",
    "max"       :   "maximum",
    "norm"      :   "sqrt(dot",
    "inv"       :   "linalg.inv",
    "pinv"      :   "linalg.pinv",
    "rank"      :   "linalg.matrix_rank",
    "conjgrad"  :   "Sci.linalg.cg",
    "disp"      :   "print",
}

operators={
    "&&"    :   " and ",
    "||"    :   " or ",
    "~"     :   "!",
    "~="    :   "!=",
    ".^"    :   "**",
    "^"     :   "**",
    ".*"    :   "*",
}

def convertOp(op):
    if op in operators:
        op =  operators[op]
    return op

def convertFunc(func):
    if func in functions:
        func = functions[func]
    return func
