from collections import Counter

# :::::::::::::::::THIS IS FOR SINGLE MAX VALUE:::::::::::::::::::
# a=input("enter setence:")
# b=Counter(a)
# print(b)
# m=max(b, key = b.get)
# print(f"key{m} is occuring maximum time which is {b[m]}")

# :::::::::::::::::THIS IS FOR MULTIPLE MAX VALUE:::::::::::::::::::
# a=input("enter setence:")
# b=Counter(a)
# m=max(b.values())
# mk=[k for k,v in b.items() if v==m]

# print(f"keys with maximum values are",mk)



# ****************WORD OF MAXIMUM LENGHT************
a=input("enter setence:").split()
print(a)
mv=0
mn=""
for i in a:
    if(len(i)>mv):
        mv=len(i)
        mn=i


print(f"word of maximum lenght is {mn} having length {len(mn)}  ")   
