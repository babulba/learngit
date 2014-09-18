
def makeDataSet(fileName):
    tSet = []
    fileDescriptor = open(fileName)
    
    for fLine in fileDescriptor:
        fLine=fLine.strip()
        if "?" in fLine:
            continue
        idnum,a1,a2,a3,a4,a5,a6,a7,a8,a9,diag=fLine.split(",")
        patientTurple=(idnum,diag,int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9))
        if diag=="4":
            diagMorb="m"
        if diag=="2":
            diagMorb="b"
        patientTurple=(idnum,diagMorb,int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9))
        tSet.append(patientTurple)
    return tSet

def sumLists(list1,list2):
    sumList=[0.0]*9
    for index in range(0,9):
        sumList[index]=list1[index]+list2[index]
    return sumList

def makeAverages(sumList,total):
    averageList=[0.0]*9
    total=float(total)
    for indx in range(9):
        averageList[indx]=sumList[indx]/total
    return averageList


def trainClassifier(trainingSet):
    benignSums=[0]*9
    benignCount=0
    malignantSums=[0]*9
    malignantCount=0
    
    for patientTup in trainingSet:
        if patientTup[1]=='b':
            benignSums=sumLists(benignSums,patientTup[2:])
            benignCount+=1
        else:
            malignantSums=sumLists(malignantSums,patientTup[2:])
            malignantCount+=1
    
    benignAvgs=makeAverages(benignSums,benignCount)
    malignantAvgs=makeAverages(malignantSums,malignantCount)
    
    classifier=makeAverages(sumLists(benignAvgs,malignantAvgs),float(2))
    
    return classifier

def classifyTestSet(testSet,classifier):
    results=[]
    for patient in testSet:
        benignCount=0
        malignantCount=0
        
        for index in range(0,9):
            if patient[index+2]>classifier[index]:
                malignantCount+=1
            else:
                benignCount+=1
        resultTuple=patient[0],benignCount,malignantCount,patient[1]
        results.append(resultTuple)
    return results
    return

def reportResult(results):
    totalCount = 0
    inaccurateCount=0
    for r in results:
        totalCount+=1
        if r[1]>r[2]:
            if r[3]=='m':
                inaccurateCount+=1
        elif r[3]=='b':
            inaccurateCount+=1
    print "Of",totalCount," patients,there were ",\
            inaccurateCount,"inaccuracies"
        
            
            
    return

def main():
    print "Reading in training data..."
    trainingFile="breast-cancer-wisconsin.data"
    #trainingFile="bc.txt"
    trainingSet=makeDataSet(trainingFile)
    print "Done reading training data.\n"
    #print trainingSet
    
    print "Training classifier..."
    classifier=trainClassifier(trainingSet)
    print "Done training classifier.\n"    
    
    print "Reading in test data..."
    testFile="bc.txt"
    testSet=makeDataSet(testFile)
    print "Done reading test data.\n"
    
    print "Classifying records..."
    resultList = classifyTestSet(testSet,classifier)
    print "Done classifying"
    
    reportResult(resultList)
    
    print "Program finished.\n"
main()