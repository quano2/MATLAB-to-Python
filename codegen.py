from Parse import myparser


def decode(list):
    '''
    Creates list of lines to be indented.
    :param list:
    :return:
    '''
    indents = []
    for i in list:
        for x in range(i[0],i[1]+1):
            indents.append(x)
    return sorted(indents)

def indent(code,ilist):
    '''
    Indents code at the line numbers from ilist.
    :param code:
    :param ilist:
    :return:
    '''
    temp = code.split('\n')
    for i in ilist:
        i-=1
        temp[i] = "\t"+temp[i]
    return "\n".join(temp)

def addLines(code,list):
    '''
    Adds line to code at line numbers from list, used to ensure indentation is correct.
    :param code:
    :param list:
    :return:
    '''
    newcode = code.split("\n")
    list = sorted(list)
    for i in list:
        print ("add line at",i-1,"len",len(newcode))
        newcode.insert(i-1,"")
    return "\n".join(newcode)

def removeEmpty(code):
    '''
    Will remove empty lines from code.
    :param code:
    :return:
    '''
    newcode = code.split("\n")
    counter = 0
    for i in range(len(newcode)):
        i -= counter
        if newcode[i].strip() == "":
            newcode.pop(i)
            counter += 1
    return "\n".join(newcode)

def translate(input):
    '''
    This is the translator which combines all of the other classes and methods to translate the input.
    :param input:
    :return:
    '''
    input = addSemi(input)
    output,ind,empty,coms = myparser(input)
    output = output.print()
    output = addLines(output,empty)
    de = decode(ind)
    output = indent(output,de)
    output = addComments(output,coms)
    output = removeEmpty(output)
    return output

def addSemi(input):
    '''
    Takes in a list of strings (whitespace is removed) and will add semi colons to the end of the
    strings unless the string is end. The input is then returned joined by newlines.
    :param input:
    :return:
    '''
    input = input.split('\n')
    while "" in input:
        input.remove("")   #removes empty lines
    for lineno in range(len(input)):
        input[lineno] = input[lineno].replace("end","end\n")
        input[lineno] = input[lineno].replace("%",";%")
        input[lineno] = input[lineno].strip()
        if input[lineno][-1]!= ';':
            input[lineno]+=";"
    return "".join(input).replace(";",";\n")

def addComments(code,comments):
    code = code.split("\n")
    for i in range(len(comments)):
        print ("here",type(code))
        code.insert(comments[i][0]-1,"#"+comments[i][1])
    return "\n".join(code)

if __name__=="__main__":
    code = """m = 0;
ir = 0;
il = 0;
for j=1:10
    if(124>m)
        m=er(j,j);
        ir = j;
    end
end

for j=1:15
    if(156>m)
        m=el(j,j);
                il = j;
    end
end

"""

    code  = addSemi(code)
    print(code)
    output,ind,empty,comments = myparser(code,debug=0)
    print(code)
    output = output.print()
    output = addLines(output,empty)
    de = decode(ind)
    output = indent(output,de)
    output = addComments(output,comments)
    output = removeEmpty(output)

    #output = translate(code)
    file = open("newfile.py","w")
    file.write(output)
    file.close()