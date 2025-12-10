def sum(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s

p=int(input("enter number"))
print(p)
print(sum(p))
    