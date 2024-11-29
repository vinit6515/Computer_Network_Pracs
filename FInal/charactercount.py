n = int(input('Enter the number of frames: '))
stuffed_string=""
for i in range (0,n):
    frame = input("Enter the frame value")
    l = len(frame)+1
    stuffed_string = stuffed_string + f"{l}{frame}"
print(stuffed_string)