print("Vinit Shah C183 60004220097 C3-2")
n=int(input("Enter number of frames:"))
str=""
for i in range(0,n):
    text=input(f"Enter frame {i+1}:")
    str+=f"{len(text)+1}"+text
print("Stuffed String : "+str)
