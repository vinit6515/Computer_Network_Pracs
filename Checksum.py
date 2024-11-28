def crc_checksum(data, divisor):
    # Append zero bits to the data (same length as divisor minus one)
    padded_data = data + '0' * (len(divisor) - 1)
    remainder = list(padded_data)

    # Perform division (XOR with divisor)
    for i in range(len(data)):
        if remainder[i] == '1':  # Only divide when the current bit is 1
            for j in range(len(divisor)):
                remainder[i + j] = str(int(remainder[i + j]) ^ int(divisor[j]))

    # The remainder is the CRC checksum
    return ''.join(remainder[-(len(divisor) - 1):])

# Example usage
data = input("Enter data bits: ")  # Example: '11010011101100'
divisor = input("Enter divisor (polynomial): ")  # Example: '1011'

checksum = crc_checksum(data, divisor)
print("CRC Checksum:", checksum)
