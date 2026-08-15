raw_data = "SRV-01,200,192.168.1.1;SRV-02,500,192.168.1.2;SRV-03,403,192.168.1.3"

def Transform_data(raw_logs):
     
    Struct_List = []

    print("Starting to transnform data")
    
    serverblock = raw_logs.split(";")

    for block in serverblock:
          cut = block.split(",")
          Server = cut[0]
          Code = int(cut[1])
          ip = cut[2]

          server_dict = {
            "server_id": Server,
            "status_code": Code,
            "ip": ip
        }
          Struct_List.append(server_dict)

    return Struct_List


          
def main():
    structured_data = Transform_data(raw_data)
    print(structured_data)
     

if __name__ == "__main__":
      main()