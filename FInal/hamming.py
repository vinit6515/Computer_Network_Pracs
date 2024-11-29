hamming = input("Enter the 9-bit hamming code : ")
h = [int (b) for b in hamming]
p1 = ( h[0] + h[2] + h[4] +h[6] + h[8])%2
p2 = (h[7]+ h[2]+h[3]+h[6])%2
p4=(h[3]+ h[4]+h[5]+h[2])%2
p8= (h[0]+h[1])%2
error_bianry = f"{p8}{p4}{p2}{p1}"
error_decimal = int (error_bianry,2)
print(f"Error at place: {error_decimal}")
hamming_list = list(h)
if hamming_list[(error_decimal-1)]==1:
    hamming_list[(error_decimal-1)]=0
elif hamming_list[(error_decimal-1)]==0:
    hamming_list[(error_decimal-1)]=1
print(hamming_list)
