mt=input()
str=list(mt)
rt=[]
st=[]
for i in range(len(str)):
    if str[i]=='1':
        for j in range(i, len(str)):
            rt.append(str[j])   
        break
rt=rt[::-1]
for i in range(len(rt)):
    if rt[i]=='1':
        for j in range(i, len(rt)):
            st.append(rt[j])   
        break
if '0' in st:
    print("NO")
else:
    print("YES")









