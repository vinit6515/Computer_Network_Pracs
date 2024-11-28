print("Character Count Technique")
n=int(input("Enter number of frames:-"))
str=""
for i in range(0,n):
    text=input(f"Enter frame {i+1}:")
    str = str + f"{len(text)+1}" + text
print(f"Stuffed String : {str} ")
print("\n")
print("We are implementing bit stuffing framing technique")
def main():
    bit_stuffing()
#It has 4 rules basically:
#1. A FLAG B => A ESC FLAG B
#2. A ESC B => A ESC ESC FLAG B
# 3. A ESC FLAG B => A ESC ESC ESC FLAG B 
# 4. A ESC ESC B => A ESC ESC ESC ESC B 
def byte_stuffing():
    str=input("Enter the string: ")
    esc = input("Enter the escape scharacter: ")
    flag = input ("Enter the flag character: ")
    text=""
    for i in str:
        if i == esc: # This is for rule 1
            text+= (esc + i) 
        elif i == flag :
            text  += (esc + i) 
        else:
            text += i
    print(f"Stuffed String : {text} ")
if __name__=="__main__":
    main()

def bit_stuffing():
    print("We are now gonna implement bit stuffing:")
    #Bit Stuffing Technique
    #If there are 5 consecutive 1's add 0
    str= input("Enter the string: ")
    text=""
    for i in range(0,len(str)):
        ch= str[i]
        if ch=='1':
            if str[i-1]=='0':
                count=0
            else:
                count+=1
        else:
            count=count-1
        if count==5:
            text=text+'0'
        text=text+ch
    print(f"Stuffed String : {text}")

