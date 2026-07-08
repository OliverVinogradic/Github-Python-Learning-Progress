def parse_data(raw_string):
    clean_list = []
   
    serverblock = raw_string.strip().split(";")
    
    for block in serverblock:
        cut = block.split(",")
        s_name = cut[0]
        e_code = int(cut[1])
        s_ip = cut[2]

        new_dict = {
            "Server Name": s_name,  
            "Error Code": e_code,
            "Server IP": s_ip, 
        }
        clean_list.append(new_dict)

    return clean_list

def filter_errors(logs):
    alarm_list = [] 
    for server in logs:
        servercode = server.get("Error Code")
          
        if servercode >= 400:
            
            server_ip = server.get("Server IP")
            alarm_list.append(server_ip) 
            
    return alarm_list

def main():
  
    with open("logs.txt", "r") as file:
        data_from_txt = file.read()
    
  
    mid_res = parse_data(data_from_txt)
    result = filter_errors(mid_res)

    print("Kritische IPs aus Datei gefiltert:", result)

if __name__ == "__main__":
    main()