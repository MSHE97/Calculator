# -*- coding: utf-8 -*-

import sys

class IOFiles:
    inputFile = sys.argv[1]
    writeFile1 = "PositiveResults.txt"
    writeFile2 = "NegativeResults.txt"

class calc:
    def calculate(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                pass
            else:
                return a / b

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
    for line in f:
        space = line.find(' ')
        a = float( line[:space] )
        b = float( line[ space + 1:] )
        result = myCalc.calculate(a, b, sys.argv[2])
        if result >= 0:
            wrFilePos.write( str(result) + '\n' )
        else:
            wrFileNeg.write( str(result) + '\n' )
    f.close()
    wrFilePos.close
    wrFileNeg.close

if __name__ == '__main__':
    main()