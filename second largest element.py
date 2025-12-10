# a=[int (x) for x in int(input("enter list:").split())]
# a=[int (x) for x in (input("enter list:").split())]
# print("your list is::",a)
# //1st method//*
# b=max(a)
# a.remove(b)
# c=max(a)
# print(c)
# # for i in a:
#     # if (i!=b):
#     #     c=max
# # print (b)
# # for i in a:


# //2nd  method//*

# num=int(input("enter number of element:"))
# a=[]
# for i in range (num):
#     val=int(input(f"enter number {i+1}: "))
#     a.append(val)
    
# print(a)
# a.sort()
# print("second largest element is::",a[-2])

# apporiate way
a=[int (x) for x in input("enter list:").split()]
print(a)
a.sort()
print("sorted list is:",a)
print("second largest element is::",a[-2])
