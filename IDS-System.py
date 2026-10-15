import time

def main():
    temp_list = []  
    with open("server_access.log","r") as file:
        for line in file:
            wholeline = line.strip()
            time.sleep(1)
            print(line)
            for l_parts in wholeline:
                l_parts = line.split("-")
                time.sleep(1)
                print(l_parts)

if __name__ == "__main__":
    main()