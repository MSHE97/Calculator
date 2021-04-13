# -*- coding: utf-8 -*-

import sys

class IOFiles:
    inputFile = sys.argv[1]
    writeFile1 = "PositiveResults.txt"
    writeFile2 = "NegativeResults.txt"

class calc:
    err = 0
    def calculate(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                self.err = -1
                pass
            else:
                return a / b
        else:
            self.err = -2
            

def main():
    myFiles = IOFiles()
    myCalc = calc()
    try:
        f = open(myFiles.inputFile)
    except IOError:
        input("Can't find such file. Please, press enter to exit")
        return
    wrFilePos = open(myFiles.writeFile1, 'w')
    wrFileNeg = open(myFiles.writeFile2, 'w')
    operation = sys.argv[2] 
    for line in f:
        space = line.find(' ')
        a = float( line[:space] )
        b = float( line[ space + 1:] )
        result = myCalc.calculate(a, b, operation)
        if myCalc.err == -1:
            errMsg = "Be caruful, dividing zero!\n"
            print(errMsg)
            if a > 0:
                wrFilePos.write(errMsg)
            else:
                wrFileNeg.write(errMsg)
            myCalc.err = 0
            continue
        if myCalc.err == -2:
            errMsg = "Indefined operation '{}'\n".format(operation)
            print(errMsg)
            wrFilePos.write(errMsg)
            wrFileNeg.write(errMsg)
            break
        if result >= 0:
            wrFilePos.write( str(result) + '\n' )
        else:
            wrFileNeg.write( str(result) + '\n' )
    f.close()
    wrFilePos.close
    wrFileNeg.close

if __name__ == '__main__':
    main()