a=[int (x) for x in input("enter list:").split()]
even=[]
odd=[]
e=0
o=0
for i in a:
    if(i%2==0):
        e+=1
        even.append(i)
    else:
        o+=1
        odd.append(i)
print(f"even list is:{even},total even numbers:{e}")
print(f"odd list is:{odd},total odd numbers:{o}")

# appropriate way
a=[int (x) for x in input("enter list:").split()]
e=0
o=0
for i in a:
    if(i%2==0):
        e+=1    
    else:
        o+=1

print(f"total even numbers:{e}")
print(f"total odd numbers:{o}")
