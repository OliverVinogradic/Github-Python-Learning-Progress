
#Opening the bit text file and transfering its data
def bin_txt_trans():
        Bin_list = []
        try:
            with open("bin.txt","r") as data_bin:
                number_count = 0
                Bin_octet = data_bin.read()
                for bin in Bin_octet:
                     if bin.isdigit():
                      number_count +=1
                     else:
                         print("Unknow Error")
    
            dev_num = number_count // 8
            for i in range(dev_num):
             Bin_list.append(Bin_octet[:8])
    
    
        except FileNotFoundError:
            print("File not Found")
        
        return Bin_list
    
    

def main():
    print("Main function start")
    
   

if __name__ == "__main__":
    main()
