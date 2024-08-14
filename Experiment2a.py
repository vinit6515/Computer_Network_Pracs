print("Vinit Shah   C183 60004220097")
str=input("Enter string:")
sf=input("Enter start flag:")
ef=input("Enter end flag:")
esc=input("Enter escape flag:")
text=""
text+=sf
for i in str:
    if i==sf:
        text+=(esc+i)
    elif i==ef:
        text+=(esc+i)
    elif i==esc:
        text+=(esc+i)
    else:
        text+=i
text+=ef
print("Stuffed String : "+text)
