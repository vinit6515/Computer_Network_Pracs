data = input("Enter the string followed by , : ")
array = data.split(",")
esc = input ("Enter the escape character : ")
flag = input('Enter the flag character : ')
stuffed_string=[]
for byte in array:
    if byte == esc or byte== flag:
        stuffed_string.append(esc)
    stuffed_string.append(byte)
print(f"Stuffed String : {stuffed_string}")