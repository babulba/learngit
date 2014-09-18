def addWord(w,theSet):
    if len(w)>3:
        theSet.add(w)
        

import string
def processLine(line,theSet):
    line=line.strip()
    wordList=line.split()
    for word in wordList:
        if word !='--':
            word=word.lower()
            word=word.strip(',.')
            word=word.strip(string.punctuation)
            addWord(word,theSet)  
           
                

def prettyPrint(gaSet,doiSet):
    print 'Count of unique words of length 4 or greater'
    print 'Gettysburg Addr:%d,Decl of Ind:%d\n'%(len(gaSet),len(doiSet))
    print 
   
          
def main():
    theSet={}
    fObj=open("1.txt","r")
    for line in fObj:
        processLine(line,theSet)
    print('Length of the dictionary:',len(theSet))
    prettyPrint()

main()




        


