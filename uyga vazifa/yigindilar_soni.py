a=int(input())
count=0
for i in range(a+1):
    for j in range (i+1, a+1):
        if i+j==a:
            count+=1
            
print(count)