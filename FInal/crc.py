#Cyclin Redundancy Check
data = input("Enter the data bits: ")
divisor = input ("Enter the divisor: ")
def checksum(data,divisor):
    padded_data = data + '0'*(len(divisor)-1)
    remainder = list(padded_data)
    for i in range(len(data)):
        if remainder[i] == '1':
            for j in range(len(divisor)):
                remainder[i+j] = str(int (remainder[i+j]) ^ int (divisor[j]))
    return ''.join(remainder[-(len(divisor)-1):])
print(f"CheckSum : {checksum(data , divisor)}")