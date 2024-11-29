string = input('Enter the string you want to send : ')
count = 0 
text = ""
for i in range ( 0, len(string)):
    ch = string[i]
    if ch == '1':
        if string[i-1]=='0':
            count = 0 
        else :
            count = count + 1
    if count == 5 :
        text = text + f"0"
        count = 0
    text = text + ch
print(text)