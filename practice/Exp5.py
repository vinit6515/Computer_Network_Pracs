#We are implementing program to find subnet and class of given ip addrerss
def find_subnet_mask_and_class():
    ip_add= input("Enter the IP address: ")
    octets = ip_add.split(".")
    first_octet= int(octets[0])
    if 0<= first_octet<= 127:
        subnet_mask="255.0.0.0"
        subnet_class="A"
    elif 128<= first_octet <= 191:
        subnet_mask="255.255.0.0"
        subnet_class="B"
    elif 192<= first_octet <= 224:
        subnet_mask="255.255.255.0"
        subnet_class="C"
    elif 225<= first_octet <= 238:
        subnet_mask="Reserved for multicasting"
        subnet_class="D"
    elif 239<= first_octet <= 255:
        subnet_mask="Reserved for Special Networks"
        subnet_class="E"
    else:
        subnet_mask="Invalid"
        subnet_class="Invalid"
    return subnet_class, subnet_mask
def main():
    subnet_class , subnet_mask= find_subnet_mask_and_class()
    print(f"Subnet Mask : {subnet_mask} \nSubnet Class: {subnet_class}")
if __name__=="__main__":
    main()
