from collections import Counter
a=input("enter first word:")
b=input("enter second word:")

if(Counter(a)==Counter(b)):
  print(f"{a} and {b} are anagrams")
else:
  print("Not anagrams")

