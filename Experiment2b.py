print("Vinit Shah C3-2 C183 60004220097")
str=input("Enter string:")

text=""
count=-1
for i in range(0,len(str)):
    ch=str[i]
    if ch=='1':
        if i!=0:
            if str[i-1]==0:
                count=0
            else:
                count+=1
    else:
        count=-1
    
    if count==5:
        text+='0'
    text+=ch   
print(text)
