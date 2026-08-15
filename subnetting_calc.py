

def u_ip_input():
    while True:

        u_ip_in = input("Write your IPv4 Adress inside the terminal\n")
        ip_octet = u_ip_in.split('.')

        if len(ip_octet) != 4:
         print("IPv4 didint passed the length test try again\n")
         continue

        try: 
         int_octest = [int(o) for o in ip_octet]
        except ValueError:
           print("The IP adress can only contain Int values\n")
           continue

        if all(0 <= o <=255 for o in int_octest):
           return int_octest
        else:
           print("The Int Values in the Octets are either to high or to low..\n")
           continue
    

    
                
      




def main():
 print("lol")
 result = u_ip_input()
 print(result)

if __name__  ==  "__main__":
    main()