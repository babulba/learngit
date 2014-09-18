def addWord(w,wcDict):
    if w in wcDict:
        wcDict[w]=wcDict[w]+1
    else:
        wcDict[w]=1

import string
def processLine(line,wcDict):
    line=line.strip()
    wordList=line.split()
    for word in wordList:
        if word !='--':
            word=word.lower()
            word=word.strip(',.')
            word=word.strip(string.punctuation)
            addWord(word,wcDict)  
           
                

def prettyPrint(wcDict):
    valKeyList=[]
    for key,val in wcDict.items():
        valKeyList.append((val,key))
    valKeyList.sort(reverse=True)
    print('%-10s%10s'%('Word','Count'))
    print('_'*21)
    for val,key in valKeyList:
        print('%-12s    %3d'%(key,val))
        
'''import codecs    '''    
def main():
    wcDict={}
    fObj=open("1.txt","r")
    '''if fObj[:3] == codecs.BOM_UTF8:  
        fObj = fObj[3:] '''
    for line in fObj:
        processLine(line,wcDict)
    print('Length of the dictionary:',len(wcDict))
    prettyPrint(wcDict)

main()
'''  
    for line in fObj:
        line=line.strip()
        lineList=line.split()
        print("%-15s %15s"%(lineList[0],lineList[1]))
'''        
         

        




'''
def makeWordList(gFile):
    speech=[]
    for lineString in gFile:
        lineList=lineString.split()
        for word in lineList:
            word=word.lower()
            word=word.strip(',.')
            if word!="--":
                speech.append(word)
    return speech
    
def makeUnique(speech):
    unique=[]
    for word in speech:
        if word not in unique:
            unique.append(word)
    return unique
    
unique=makeUnique(speech)
print(unique)
print("Unique Length:",len(unique))
'''



        


