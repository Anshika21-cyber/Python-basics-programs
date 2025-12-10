# from collections import counter
name=input("enter names:").split()
print(name)
# Counter(name)
dict={}
marks=[int (x) for x in input("enter marks").split()]
print(marks)
for i in range(len(name)):
    dict[name[i]]=marks[i]
    
       


print(dict)