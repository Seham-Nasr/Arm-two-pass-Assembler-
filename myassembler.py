#! python3
from assembly import *
import sys
def main():
    
    fname = sys.argv[1]
    listingfile=sys.argv[3]

    f = open(fname, 'r')
    symFile = open(listingfile,"w")        
    text = f.read()
    text =text.split('\n')
   
    displayText = ''
    for i in range(len(text)):
        displayText += (str(i + 1) + ' ' + text[i] + '\n')   #
    #print(displayText)
    lineNo, assembledCode, errorList, errorFlag = assemble(displayText)

    if errorFlag is False:
        outputText = ''
        print('\tAssembled...\n')
        for i in range(len(assembledCode)):
            outputText += (str(i + 1) + ' ' + assembledCode[i] +'\n')
        symFile.write(outputText)
        symFile.write("\n")
        symFile.close() 

    else:
        infoString = str(len(errorList)) + ' Errors.\n'
        for i in errorList:
            ##print(i)
            infoString += ('Error at line: ' + str(i.get('lineNo')) + '\nType: ' + str(i.get('type')) + '\n\n')
       
        
if __name__ == '__main__':
   main()                