data = input("Enter the dividend: ")
divisior = input ("Enter the divisor :")
def checksum(data , divisor):
    padded_data = data + '0'*(len(divisior)-1)
    remainder = list(padded_data)
    for i in range(len(data)):
        if remainder[i]=='1':
            for j in range(len(divisior)):
                remainder[i+j]= str(int(remainder[i+j]) ^ int(divisor[j]))
    return ''.join(remainder[-(len(divisior)-1):])
print(f"Checksum: {checksum(data,divisior)}")