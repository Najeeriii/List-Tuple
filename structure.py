list1=[]
list2=list()
print(list1)
list1.append("Twenty")
list1.append(3.1)
list1.append(20)
list1.append(True)
print(list1)
print(list1.index(20))
list1[3]=False
print(list1)
print(len(list1))
list1.remove(False)
print(list1)
a=list1.pop(2)
print(a)
print(list1)
list2=[2,122,24,33,890]
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.clear()
print(list2)