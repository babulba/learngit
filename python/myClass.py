class myClass(object):
    def method1(self,theTuple):
        self.localList=[]
        for element in theTuple:
            if element >10:
                self.localList.append(element)
                
    def method2(self):
        self.theSum=0
        for element in self.localList:
            self.theSum+=element
        return self.theSum
    

inst1=myClass()
inst2=myClass()
inst1.method1([1,2,3])
print inst1.localList

inst1.method1([10,11,12])
print inst1.localList
print inst1.method2()


#inst2.method2()