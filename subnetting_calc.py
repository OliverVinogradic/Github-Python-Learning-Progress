

def u_ip_input():
    while True:

        u_ip_in = input("Write your IPv4 Adress inside the terminal\n")
        ip_octet = u_ip_in.split('.')

        if len(ip_octet) != 4:
         print("IPv4 didin't pass the length test try again\n")
         continue

        try: 
         int_octets = [int(o) for o in ip_octet]
        except ValueError:
           print("The IP adress can only contain Int values\n")
           continue

        if all(0 <= o <=255 for o in int_octets):
           return int_octets
        else:
           print("The Int Values in the Octets are either too high or to low..\n")
           continue
    

    
def u_cidr_input():
    while True:
         try:
            cidr_input = int(input("Enter your Cidr Number TIP(1-32)\n"))
            if cidr_input >= 1 and cidr_input <= 32:
               print("Your Cidr Input is correct\n")
               return cidr_input
            else:
               print("The Int input is either too high or too low...\n")
         except ValueError:
            print("Enter Int Values\n")
            continue
        
def cidr_to_netmask(cidr):
    host_bits = 32 - cidr
    mask_32bit = ((1 << cidr) - 1) << host_bits

    octet1 = (mask_32bit >> 24) & 0xFF
    octet2 = (mask_32bit >> 16) & 0xFF
    octet3 = (mask_32bit >> 8) & 0xFF
    octet4 = mask_32bit & 0xFF

    return [octet1, octet2, octet3, octet4]



def main():
 print("lol")
 ip_result = u_ip_input()
 print(ip_result)
 cidr_result = u_cidr_input()
 print(f"Cidr Result {cidr_result}")
 netmask_result = cidr_to_netmask(cidr_result)
 print(f"Netmask Result {netmask_result}")

if __name__  ==  "__main__":
    main()