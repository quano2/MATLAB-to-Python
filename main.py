from codegen import translate

openmsg = '''#The code below has been translated from MATLAB to Python using Quano's translator.
from numpy import *
from Scipy import *\n'''

if __name__=="__main__":
    #filename = input("Please enter a filename to translate\n")
    filename = "testfile"
    try:
        file = open(filename+".txt",'r')
        print("Reading in file: %s"%filename)
        input = file.read()
        file.close()
        output = translate(input)
        fileout = open(filename+".py","w")
        fileout.write(openmsg+output)
        fileout.close()
    except FileNotFoundError as e:
        print("Your file: %s, has not been found, please check the filename and try again."%filename)