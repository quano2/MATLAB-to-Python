from Parse import myparser

def convert(code):
    if isinstance(code,str):
        return code
    newcode = '\n'.join(code)
    return newcode

def decode(list):
    indents = []
    for i in list:
        print(i)
        for x in range(i[0],i[1]+1):
            print (x)
            indents.append(x)
    return sorted(indents)

def indent(code,ilist):
    temp = code.split('\n')
    for i in ilist:
        i-=1
        temp[i] = "\t"+temp[i]
    return "\n".join(temp)


def translate(input):
    output,ind = myparser(input)
    de = decode(ind)
    output = indent(output,de)
    return output

def addSemi(input):
    '''
    Takes in a list of strings (whitespace is removed) and will add semi colons to the end of the
    strings unless the string is end. The input is then returned joined by newlines.
    :param input:
    :return:
    '''
    while "" in input:
        input.remove("")   #removes empty lines
    for lineno in range(len(input)):
        input[lineno] = input[lineno].strip()
        input[lineno] = input[lineno].replace("end","end\n")
        if input[lineno][-1]!= ';':
            input[lineno]+=";"
    return "".join(input).replace(";",";\n")

if __name__=="__main__":
    code = """while n>5
    n= n-1
    while n>5
    f= f*n
    for o = 7:9;i=9;end
    end
    end
"""
    code = code.split('\n')
    code = addSemi(code)
    output,ind = myparser(code,debug=0)

    output = output.print()
    print (output)

    de = decode(ind)

    output = indent(output,de)
    print ("output is\n",output)

    file = open("newfile.py","w")
    file.write(output)
    file.close()