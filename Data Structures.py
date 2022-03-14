# 1)Return all the duplicate values from list of arraylist

myList1=[[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
for subList in myList1:
    mySet=set(subList)
    for item in mySet:
        countOfItem=subList.count(item)
        if(countOfItem>1):
            print(item,"->",countOfItem,end=" ")
    print()
print()


# 2)Merge two lists as shown below 


list1 = ["Hello ", "take "] 
list2 = ["Dear", "Sir"] 
list3 = list1 + list2
print(list3)


# 3) Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list 

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList=["h", "i", "j"]
list1[2][1][2].extend(subList)
print(list1)

# 4) Map the dictionary in the following manner

Keys = ['Ten', 'Twenty', 'Thirty'] 
Value = [10,20,30]
res = dict(zip(Keys, Value)) 
print(res)


# 5)  Merge following two Python dictionaries into one 

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 

dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50} 
dict1.update(dict2)
print(dict1)


# 6)  Rename key city to location in the following dictionary 

sampleDict = { 

  "name": "Kelly", 

  "age":25, 

  "salary": 8000, 

  "city": "New york" 

}


new_key = "location"
old_key = "city"
sampleDict[new_key] = sampleDict.pop(old_key)

print(sampleDict)


# 7) Convert Dictionary to list 

sampleDict={'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
newList=[]
for k,v in sampleDict.items():
    newList.append(list(k.split())+list(sampleDict[k]))
print(newList)
