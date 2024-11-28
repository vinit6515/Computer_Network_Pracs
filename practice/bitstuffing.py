data = input("Enter the character sequence : ")
count =0
text="" 
for i in range(0,len(data)):
    ch=data[i]
    if ch=='1':
        if data[i-1] =='0':
            count=0
        else:
            count=count+1
    if count == 5 :
        text= text+"0"
        count = 0
    text= text + ch
print(f"Stuffed String : {text}")