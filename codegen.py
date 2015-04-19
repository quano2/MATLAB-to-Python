from Parse import myparser

def convert(code):
    if isinstance(code,str):
        return code
    newcode = '\n'.join(code)
    return newcode

def decode(list):
    indents = []
    for i in list:
        for x in range(i[0],i[1]+1):
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
        input[lineno] = input[lineno].replace("end","end\n")
        input[lineno] = input[lineno].strip()
        if input[lineno][-1]!= ';':
            input[lineno]+=";"

    return "".join(input).replace(";",";\n")

if __name__=="__main__":
    code = """try
for x=0:90
    c = 9
    p=0
    for i = 0:10
        p=0
        for i = 0:10
            q= 0
            u=7
        end
        q=i
        p=8
        l=0
        for i=0:10
            p=9
            u=9
        end
    end
    asd =l
    p=9
end
catch ME
for i = 0:10
    o=p
    o=8
end
for i = 0:10
    i=8
end
for i =0:10
    p=0
end
end"""

    code = code.split('\n')
    code = addSemi(code)

    output,ind = myparser(code,debug=0)

    output = output.print()
    print (output)

    de = decode(ind)
    print (de)
    output = indent(output,de)
    print ("output is\n",output)

    file = open("newfile.py","w")
    file.write(output)
    file.close()