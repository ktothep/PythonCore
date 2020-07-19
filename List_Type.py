#Empty List
list=[]
list.append("One")
list.append("two")
list.append("Four")
list.append("Five")

#Printing List
print(list)

#list loop
for j in list:
    print(j)

#particular Element
print(list[1])

#Slicing
list.append("Three")
print(list[:2])
print(list[1:3:2])

#shallowcopy
list_copy=list
print(list_copy)
list.remove("One")
print(list_copy)

#Deepcopy
list_deep=[]
for i in range(len(list)):
    list_deep.append(list[i])
print("First iteration before deletion")
print(list_deep)
list.remove("Five")
print("Second iteration after deletion")
print(list_deep)
