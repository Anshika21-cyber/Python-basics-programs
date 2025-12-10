a=[int (x) for x in input("enter list:").split()]
print("original list is:",a)
b=[0]*len(a)
j=len(a)
# for i in range(j-1,-1,-1):
#     b.append(a[i])
for i in a:
 
 b[j-1]=i
 j=j-1

print(b)    