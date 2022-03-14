from itertools import combinations
from collections import Counter

class StringClass:
    def __init__(self,st):
        self.st = st
    def length(self):
        return len(self.st)
    def strToList(self,stt):
        L=list(stt)
        return L

obj=StringClass('12314532')
print("Length of a string: ",obj.Length())
print("String to List: ",obj.strToList('12314532'))



class PairsPossible(StringClass):
    res=[]
    def __init__(self,StringClass):
        self.st2 = StringClass.st
        
    def pairs(self):
        self.res = list(combinations(self.st2, 2))
        print("possible pairs stored")
        return self.res
    def display(self):
        print("Possible pairs: ",self.res)



p=PairsPossible(obj)
lst=[]
lst=p.pairs()
p.display()

class SearchCommonElements(PairsPossible):
    def __init__(self,st3,PairsPossible):
        self.st3=st3
        self.st=PairsPossible.st2
        
    def common(self):
        ar1 = Counter(self.st3)
        ar2 = Counter(self.st)
        resultDict = dict(ar1.items() & ar2.items())
        common = []
        for (key,val) in resultDict.items():
            for i in range(0,val):
                common.append(key)
        return common

s=SearchCommonElements("123456",p)
cm=s.common()



class EqualSumPairs():
    def summ(self,L):
        s=0
        for i in L:
            s+=int(i)
        return s
    def find(self):
        cnt=0
        for i in range(len(lst)):
            temp=self.summ(lst[i])
            for j in range(i+1,len(lst)):
                flag=0
                if temp==self.summ(lst[j]):
                    flag=1
                    break
            if flag==0:
                cnt+=1
        return cnt
    def display(self,count):
        print("Output of Search Common elements: ",lst)
        print("Equal sum pairs: ",count)

e=EqualSumPairs()
count=e.find()
e.display(count)
    
        
