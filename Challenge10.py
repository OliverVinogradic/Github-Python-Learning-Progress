def get_parse_logs(raw_string):
    clean_list = []
   #split into lines
    lines = raw_string.strip().split("\n")
    
    for line in lines:
        if not line.strip(): 
            continue 
            
        try:
            cut = line.split(",")
            
           
            if len(cut) < 3:
                continue
                
            s_name = cut[0]
            e_code = int(cut[1]) 
            s_ip = cut[2]

            new_dict = {
                "Server Name": s_name,  
                "Error Code": e_code,
                "Server IP": s_ip,
            }
            clean_list.append(new_dict)
            
        except (ValueError, IndexError):
            print(f"Broken Line ignored -> {line}")
            continue

    return clean_list

def filter_errors(logs):
    alarm_list = [] 
    for server in logs:
        servercode = server.get("Error Code")
          
        if servercode >= 400:
            
            server_ip = server.get("Server IP")
            alarm_list.append(server_ip) 
            
    return alarm_list

def write_alerts(critical_ips, filename):
    with open(filename,"w") as file:
      for ip in critical_ips:
          file.write(ip + "\n")



def main():
    
    with open("wrong_logs.txt", "r") as file:
        wrong_data = file.read()
        
    
    clean_data = get_parse_logs(wrong_data)
    
  
    defect_ips = filter_errors(clean_data)
    
   
    write_alerts(defect_ips, "critical_ips.txt")
    print("Report was generated,check files!")



if  __name__ == "__main__":
    main()