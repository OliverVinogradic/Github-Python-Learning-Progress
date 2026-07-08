raw_data = "SRV-01,200,192.168.1.1;SRV-02,500,192.168.1.2;SRV-03,200,192.168.1.3;SRV-04,404,192.168.1.4"

def parse_data(raw_string):
  clean_list = []
  serverblock = raw_string.split(";")
  for block in serverblock:
     cut = block.split(",")
     s_name = cut[0]
     e_code = int(cut[1])
     s_ip = cut[2]

     new_Dict = {
     "Server Name" : s_name ,  
     "Error Code" : e_code,
     "Server IP" : s_ip,
     }
     clean_list.append(new_Dict)

  return clean_list
  




def filter_errors(logs):
    alarm_list = [] 
    for server in logs:
        servercode = server.get("Error Code")
          
        if servercode >= 400:
         serverid = server.get("Server Name")
         serverip = server.get("Server IP")
         alarm_text = f" Server has an error. Server IP = {serverip} ."
         alarm_list.append(alarm_text)
    return alarm_list

def main():
   mid_res = parse_data(raw_data)
   result = filter_errors(mid_res)
   print(result)

if __name__ == "__main__":
   main()
 