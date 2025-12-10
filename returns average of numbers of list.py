def average(l):
    b=len(l)
    s=0
    for i in l:
        s+=i
    c=s/b
    print(c)
    return c





a=[int (x) for x in input("enter list:").split()] 
print(a)
# print(average(a))
average(a)