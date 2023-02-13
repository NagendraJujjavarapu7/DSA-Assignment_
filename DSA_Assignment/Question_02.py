l=[1,1,2,3,3,4,5,6,6]
Unique_List = []
Duplicate_List = []
for i in l:
    if i not in Unique_List:
        Unique_List.append(i)
    elif i not in Duplicate_List:
        Duplicate_List.append(i)
print(Duplicate_List)