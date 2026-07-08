server_logs = [
    {"server_id": "SRV-01", "status_code": 200, "ip": "192.168.1.1"},
    {"server_id": "SRV-02", "status_code": 500, "ip": "192.168.1.2"},
    {"server_id": "SRV-03", "status_code": 403, "ip": "192.168.1.3"},
    {"server_id": "SRV-04", "status_code": 200, "ip": "192.168.1.4"},
    {"server_id": "SRV-05", "status_code": 404, "ip": "192.168.1.5"}
]
#Pulls the dictonarys out of the list and compares the status code
def CheckServer(logs):
     alarm_list = [] 
     for server in logs:
          servercode = server.get("status_code")
          
          if servercode >= 400:
           serverid = server.get("server_id")
           serverip = server.get("ip")
           alarm_text = f"ALARM: Server {serverid} has an error. Server IP = {serverip} ."
           alarm_list.append(alarm_text)
     return alarm_list
        
def main():
    result = CheckServer(server_logs)
    print(result)



if __name__ == "__main__":
     main()
