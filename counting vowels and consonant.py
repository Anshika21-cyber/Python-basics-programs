# &&&&&&&&& THIS IS FOR TO WRITE REPEATED VOW AND CON &&&&&&&&&&&&&&
# a=input("enter setence:")
# con=0
# consonant=[]
# v=0
# vowels=[]
# for i in a:
#     if(i==" "):
#         pass

#     elif (i in ("aeiou"or"AEIOU" )):
#         con+=1
#         consonant.append(i)

#     else:
#         v+=1
#         vowels.append(i)
# print(f"no. of consonant are {con} and list is{consonant}")
# print(f"no. of vowels  are {v} and list is{vowels}")

# &&&&&&&&&& THIS IS FOR NOT TO WRITE REPEATED VOW AND CON &&&&&&&&&&&&&&&&&

a=input("enter setence:")
con=0
consonant=[]
v=0
vowels=[]
for i in a:
    if(i==" "):
        pass

    elif (i in ("aeiou"or"AEIOU" )):
        if(i not in vowels):
            v+=1
        vowels.append(i)
        

    else:
        if(i not in consonant):
            con+=1
            consonant.append(i)
            
print(f"no. of consonant are {con} and list is{consonant}")
print(f"no. of vowels  are {v} and list is{vowels}")

