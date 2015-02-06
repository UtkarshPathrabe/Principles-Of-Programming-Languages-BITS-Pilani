import re           #FOR REGULAR EXPRESSION
import os           #FOR FILE OPERATION(os.remove)

#REMOVES ALL COMMENTS AND EXTRA SPACES FROM THE CODE

f1 = open('input.txt', 'r',1)
f2 = open('input_clean.txt','w')

for line in f1.readlines():
    if line.find('#') != -1:
        index = line.find('#')
        line = line[0:index]
        line = line + '\n' 
    line.strip()
    f2.write(line)

f1.close()
f2.close()

#DEFINING A DICTIONARY WITH INFORMATION ABOUT ALL TOKENS

tokenInfo = {
                'ABSTRACT_TYPE' : 'Abstract type keyword',
                'CLASS'         : 'Class keyword',
                'TYPE'          : 'Type keyword',
                'AUTOMATE'      : 'Automate keyword',
                'ENDAUTOMATE'   : 'End automate keyword',
                'COMMAND'       : 'Command keyword',
                'IF'            : 'if keyword',
                'THEN'          : 'Then keyword',
                'ELSEIF'        : 'Else if keyword',
                'ELSE'          : 'Else keyword',
                'ENDIF'         : 'End if keyword',
                'FOR'           : 'For keyword',
                'DO'            : 'Do keyword',
                'IN'            : 'In keyword',
                'ENDFOR'        : 'End for keyword',
                'DISPLAY'       : 'Display keyword',
                'REAL'          : 'Real data type',
                'INTEGER'       : 'Integer data type',
                'STRING'        : 'String data type',
                'LIST'          : 'List data type',
                'BETWEEN'       : 'Between operator',
                'EXCEPT'        : 'Except operator',
                ','             : 'Comma seperator',
                '|'             : 'Refer class operator',
                '_'             : 'Parameter of function',
                ':'             : 'Colon operator',
                '->'            : 'Arrow operator',
                '<-'            : 'Assignment operator',
                '&'             : 'Get parent operator',
                '@'             : '@ keyword',
                '<'             : 'less than operator',
                '<='            : 'less than equal to operator',
                '>'             : 'greator than operator',
                '>='            : 'greator than equal to operator',
                '='             : 'equal to operator',
                '!='            : 'not equal to operator',
                '+'             : 'Addition operator',
                '-'             : 'Substraction operator',
                '*'             : 'Multiplication operator',
                '/'             : 'Division operator',
                '%'             : 'Modulo operator',
                '^'             : 'Exponentiation operator',
                '['             : 'Left bracket',
                ']'             : 'Right bracket',
                '('             : 'Left Parenthesis',
                ')'             : 'Right Parenthesis',
                '"'             : 'String constant terminal',
                'AND'           : 'Logical and operator',
                'OR'            : 'Logical or operator',
                'NOT'           : 'Logical not operator'
}

#STORES DECLARED VARIABLE INFO
varInfo = {'variable_name':'variable_type'}

#STORES DEFINED FUNCTIONS
funcInfo = ['function_names']

#STORES DEFINED INSTANCES
instanceInfo = {'instance_name':'instance_type'}
            
#**********************************EMPTY LINE DETECT FUNC************************************ 
def isEmptyLine(line):
    var = re.findall('\w+',line)
    if len(var)==0:
        return True
    else:
        return False
    
#************************************CHECK VARIABLE FUNC************************************ 
def checkVarName(var):
    if re.search('[A-Za-z][A-Za-z0-9]*',var):
        return True
    else:
        return False

#****************************CHECK VARIABLE DECLARATION FUNC***************************** 
def isVarDec(var):
    if re.search('_[a-zA-Z0-9]+\s(LIST\[.*\]|ABSTRACT_TYPE|INTEGER|REAL|STRING)', var):
        return True
    else:
        return False

#****************************CHECK FUNCTION DECLARATION FUNC***************************** 
def isFuncDec(var):
    x = re.findall('\w+',var)
    if len(x)==1:
        return True
    elif len(x) > 1:
        for i in range(1, len(x)):
            if x[i] != '_':
                return False
            else:
                return True
    else:
        return False
    
#*******************************CHECKS NEW DECLARATION FUNC*************************** 
def isNewDeclaration(line):
    var = re.findall('\w+', line)
    
    if not isEmptyLine(line) and ((var[0] in tokenInfo) or (var[0] in varInfo)):
        return True
    else:
        return False

#*******************************PRINT LINE NUMBER FUNC*********************************
def printLineno():
    global lineNo
    print 'Line '+ str(lineNo) + ':'


#*********************************READ FILE FUNCTION***********************************
def readFile():
    global line, lineNo
    line = File.readline()
    lineNo += 1

#**********************************PRINT ERROR MESSAGE**********************************
def printError():
    print '\t\tSyntax Error!!!'
            
#****************************FUNCTION DECLARATION PROCESSING****************************
def process_func(line):
    word = re.findall('\w+',line)
    funcInfo.append(word[0])
    print '\t\t\t'+word[0].rjust(20)+':\t\tFunction declaration'
    for i in range(1, len(word)):
        print '\t\t\t'+word[i].rjust(20)+':\t\t'+tokenInfo[word[i]]

#****************************VARIABLE DECLARATION PROCESSING****************************
def process_var(line):
    word = re.findall('\w+',line)
    
    cond_list = '_[a-zA-Z0-9]+\sLIST\[.*\]'
    cond_integer = '_[a-zA-Z0-9]+\sINTEGER'
    cond_real = '_[a-zA-Z0-9]+\sREAL'
    cond_string = '_[a-zA-Z0-9]+\sSTRING'
    cond_abstractType = '_[a-zA-Z0-9]+\sABSTRACT_TYPE'

    if re.search(cond_list,line):
        varInfo[word[0]] = 'List type variable'
        print '\t\t\t'+'LIST'.rjust(20)+':\t\t'+tokenInfo['LIST']
        print '\t\t\t'+word[0].rjust(20)+':\t\t'+varInfo[word[0]]
        for i in range(2,len(word)):
            varInfo[word[i]] = 'List Constant'
            print '\t\t\t'+word[i].rjust(20)+':\t\t'+varInfo[word[i]]
        
    elif re.search(cond_integer,line):
        varInfo[word[0]] = 'Integer type variable'
        print '\t\t\t'+'INTEGER'.rjust(20)+':\t\t'+tokenInfo['INTEGER']
        print '\t\t\t'+word[0].rjust(20)+':\t\t'+varInfo[word[0]]

    elif re.search(cond_real,line):
        varInfo[word[0]] = 'Real type variable'
        print '\t\t\t'+'REAL'.rjust(20)+':\t\t'+tokenInfo['REAL']
        print '\t\t\t'+word[0].rjust(20)+':\t\t'+varInfo[word[0]]

    elif re.search(cond_string,line):
        varInfo[word[0]] = 'String type variable'
        print '\t\t\t'+'STRING'.rjust(20)+':\t\t'+tokenInfo['STRING']
        print '\t\t\t'+word[0].rjust(20)+':\t\t'+varInfo[word[0]]
        
    elif re.search(cond_abstractType,line):
        varInfo[word[0]] = 'Abstract type variable'
        print '\t\t\t'+'ABSTRACT_TYPE'.rjust(20)+':\t\t'+tokenInfo['ABSTRACT_TYPE']
        print '\t\t\t'+word[0].rjust(20)+':\t\t'+varInfo[word[0]]

    else:
        printError()

#******************************ABSTRACT_TYPE PROCESSING****************************    
def process_abstractType():
    global line
    printLineno()
    
    var = re.findall('\w+',line)
    
    if len(var) == 2 and checkVarName(var[1]):
        varInfo[var[1]] = "Abstract variable type"
        print '\t\t\t'+ var[0].rjust(20) +':\t\t'+tokenInfo[var[0]]
        print '\t\t\t'+ var[1].rjust(20) +':\t\t'+varInfo[var[1]]
    else:
        printError()
    return False                                #Returns UsePrev as false

#**********************************CLASS PROCESSING*******************************
def process_class():
    global line
    printLineno()

    var = re.findall('\w+',line)
    varInfo[var[1]] = 'Class variable'
    
    print '\t\t\t'+ var[0].rjust(20) +':\t\t'+tokenInfo[var[0]]
    print '\t\t\t'+ var[1].rjust(20) +':\t\t'+varInfo[var[1]]
    process_operators(line)
    
    readFile()
    while not isNewDeclaration(line) and not isEmptyLine(line):
        
        printLineno()
        if isVarDec(line):
            process_var(line)
        elif isFuncDec(line):
            process_func(line)
        else:
            printError()

        process_operators(line)        
        readFile()
    return True                                 #Returns UsePrev as true

#*******************************TYPE PROCESSING**********************************
def process_type():
    global line
    printLineno()

    var = re.findall('\w+',line)
    varInfo[var[1]] = 'TYPE variable'

    print '\t\t\t'+ var[0].rjust(20) +':\t\t'+tokenInfo[var[0]]
    print '\t\t\t'+ var[1].rjust(20) +':\t\t'+varInfo[var[1]]
    process_operators(line)

    if len(var)>2:
        for i in range(2,len(var)):
            print '\t\t\t'+ var[i].rjust(20) +':\t\t'+varInfo[var[i]]

    readFile()
    while not isNewDeclaration(line) and not isEmptyLine(line):
        printLineno()
        if isVarDec(line):
            process_var(line)
        elif isFuncDec(line):
            process_func(line)
        else:
            printError()
            
        process_operators(line)        
        readFile()
        
    return True

#****************************INITALIZING ARCHITECTURE PROCESS*************************
def isIntArchDec(line):
    var = re.findall('\w+',line)
    if var[0] in varInfo:
        return True
    else:
        return False
    
#****************************INITALIZING ARCHITECTURE PROCESS*************************

def process_initArch():
    global line
    printLineno()

    var = re.findall('\w+\(*[0-9]*\)*',line)
    print '\t\t\t'+ var[0].rjust(20) +':\t\t'+varInfo[var[0]]
    
    for i in range(1,len(var)):
        reg = re.findall('\w+\([0-9]+\)', var[i])
        if len(reg) > 0:
            reg = re.findall('\w+', var[i])
            instanceInfo[reg[0]] = var[0]+' type instance'
            print '\t\t\t'+ reg[0].rjust(20) +':\t\t'+instanceInfo[reg[0]]
            print '\t\t\t'+ reg[1].rjust(20) +':\t\tNumber of '+reg[0]+' objects.'
        else:
            instanceInfo[var[i]] = var[0]+' type instance'
            print '\t\t\t'+ var[i].rjust(20) +':\t\t'+instanceInfo[var[i]]
        
    return False

#**********************************AUTOMATE STMT DETECT***************************
def isAutomatestmt(line):
    re_automateCond = '^\s*AUTOMATE\s\w*'
    if re.search(re_automateCond,line):
        return True
    else:
        return False

#**********************************OPERATOR PROCESSING*******************************
def process_operators(line):
    regex = "\s*(?:(\d+)|(\w+)|(<=|>=|<-|->|.|,|\(|\)))"
    item = re.findall(regex,line)

    for op in item:
        if op[2] in tokenInfo:
            print '\t\t\t'+op[2].rjust(20)+'\t\t'+tokenInfo[op[2]]

#************************************PROCESS STATEMENT*******************************
def process_stmt(line):
    printLineno()
    regex = '\s*(?:(\d+)|(<\w+>\s+\w+)|(\w+)|("[^+].*")|(<=|>=|<-|->|.|,|\(|\)))'
    item = re.findall(regex,line)
        
    for op in item:
        if op[0] != '':
            print '\t\t\t'+op[0].rjust(20)+'\t\t'+'Integer constant'
            
        elif op[1] != '':
            reg = re.findall('\w+',op[1])
            if reg[0] in varInfo and reg[1] in funcInfo:
                print '\t\t\t'+'<...>'.rjust(20)+'\t\t'+'Refer Type Operator'
                print '\t\t\t'+reg[0].rjust(20)+'\t\t'+varInfo[reg[0]]
                print '\t\t\t'+reg[1].rjust(20)+'\t\t'+'Function Call'
            elif reg[0] in varInfo and reg[1] in tokenInfo:
                print '\t\t\t'+'<...>'.rjust(20)+'\t\t'+'Refer Type Operator'
                print '\t\t\t'+reg[0].rjust(20)+'\t\t'+varInfo[reg[0]]
                print '\t\t\t'+reg[1].rjust(20)+'\t\t'+tokenInfo[reg[1]]
            else:
                printError()
        
        elif op[2] != '':
            if op[2] in tokenInfo:
                print '\t\t\t'+op[2].rjust(20)+'\t\t'+tokenInfo[op[2]]
            elif op[2] in varInfo:
                print '\t\t\t'+op[2].rjust(20)+'\t\t'+varInfo[op[2]]
            elif op[2] in funcInfo:
                print '\t\t\t'+op[2].rjust(20)+'\t\t'+'Function Call'
            elif op[2] in instanceInfo:
                print '\t\t\t'+op[2].rjust(20)+'\t\t'+instanceInfo[op[2]]
            else:
                if isAutomatestmt(line):
                    varInfo[op[2]] = 'Automate process name'
                    print '\t\t\t'+op[2].rjust(20)+'\t\t'+varInfo[op[2]]
                else:
                    print '\t\t\t'+op[2].rjust(20)+'\t\t'+'Temporary Variable name'

        elif op[3]!='':
            print '\t\t\t'+op[3].rjust(20)+'\t\t'+'String constant'

        elif op[4] != '':
            if not re.search('\s',op[4]) and op[4] in tokenInfo:
                print '\t\t\t'+op[4].rjust(20)+'\t\t'+tokenInfo[op[4]]
            elif re.search('\s',op[4]):
                continue
            else:
                printError()
        
        else:
            printError()           

#************************REGEX FOR IDENTIFYING STATEMENTS***************************

re_abstractTypeCond = 'ABSTRACT_TYPE\s*\w+'
re_classCond = 'CLASS\s+[A-Za-z][A-Za-z0-9]*:\W*\n'
re_typeCond ='^\s*TYPE\w*'
re_automateCond = '^\s*AUTOMATE\s+\w*'
re_displayCond = '\s*DISPLAY.*'

#**********************************MAIN SCAN********************************

File = open('input_clean.txt','r',1)                #Opening cleaned file
lineNo = 0                                          #Initializing lineno
readFile()                                          #Reading first line from file

print '\t\t\t\tLexems\t\t\t\tTokens'

while 1:
    usePrev=False;
    if not line:                                    #Detects EOF
        print 'Scan Complete!'
        break
    
    elif isEmptyLine(line):                         #Skips empty statements
        readFile()
        continue
    
    elif re.search(re_abstractTypeCond,line):       #ABSTRACT_TYPE
        usePrev = process_abstractType()
        
    elif re.search(re_classCond,line):              #CLASS
        usePrev = process_class()

    elif re.search(re_typeCond,line):               #TYPE
        usePrev = process_type()
        process_operators(line)

    elif isIntArchDec(line):                        #ARCHITECTURE DECLARATION
        process_initArch()
        process_operators(line)
        usePrev=False
        
    else:                                           #PROCESSS AUTOMATE AND COMMAND STATEMENTS
        process_stmt(line)
        usePrev=False

    if not usePrev:
        readFile()

os.remove("input_clean.txt")
#**********************************END OF PROGRAM********************************