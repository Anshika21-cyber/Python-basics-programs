num=[]
count=0
for i in range(1,51):
    if(i%5==0):
        count+=1
        num.append(i)
    else:
        continue
print(f"numbers divisible by 5 are {num},total numbers={count}")

