string = input("Enter a string followed by ,")
array = string.split(",")
esc = input("Enter the escape: ")
flag = input("Enter the flag : ")
text = []
for byte in array:
    if byte == flag or byte == esc:
        text.append(esc)
    text.append(byte)
print(f"Text :{text}")
