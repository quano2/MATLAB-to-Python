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

def indent(code,list):
    temp = code.split('\n')
    for i in list:
        i-=1
        temp[i] = "\t"+temp[i]
    return "\n".join(temp)


def translate(input):
    output,ind = myparser(input)
    de = decode(ind)
    output = indent(output,de)
    return output



if __name__=="__main__":
    output,ind = myparser("""
    i = 6;
    for i = 5:6;
        a = i+2;
    for o = i:10;
        p = 1+6;
    for i = 1:10;
        p = 1+6;
    for i = 1:10;
        p = 1+6;
    for i = 1:10;
        p = 1+6;
    for i = 1:10;
        p = 1+6;
    for i = 1:10;
        p = 1+6;
    end
    end
    end
    end
    end
    a = a + p;
    end
    p=8;
    end""")

    output = output.print()
    print (output)

    print ("here",ind)
    de = decode(ind)
    print ('here is decoded',de)

    output = indent(output,de)
    print ("output is",output)

    file = open("newfile.py","w")
    file.write(output)
    file.close()