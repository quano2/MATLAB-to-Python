from Parse import myparser

def reduce(code,output=[]):
    for item in code:
        print ("reducing",tuple)
        if isinstance(item,tuple):
            print ("reducing",item)
            reduce(item,output)
        elif isinstance(item,str):
            if code not in output:
                output.append(code)
                print (code)
    return output


#r= reduce(('a','=','5'))
r = reduce((('a', '=', ('5.0', '+', '10.0')), ('b', '=', ('99.0', '/', '2.0'))))

print ("\n\n",r)
def gencode(code):
    for line in code:
        print (len(line),line)
        for char in line:
            print (type(char))
    return False

def convert(code):
    newcode = ' '.join(code)
    return newcode

#output = myparser('''a = 5 + 10;
#b=99/2;c=4+2;''')
#print (output)

#if output:
#    print ("start")
#    gencode(output)


