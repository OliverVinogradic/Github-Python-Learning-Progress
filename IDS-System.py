import time




def transform_logs(temp_result_list):

     for row in temp_result_list:
    
        ipadress = row[0]
        date = row[1]
        http_m = row[2]
        s_code = row[3]

        temp_dict = {
            "IP_Adress": ipadress,
            "Date & Time": date,
            "HTTP Methode & Path": http_m,
            "Status Code": s_code
        }
    
        print(temp_dict)
        return temp_dict

def extract_logs():
    temp_result_list = []
    with open("server_access.log","r") as file:
        for line in file:
            cleaned_line = line.strip()

            if not cleaned_line:
               continue
            data = cleaned_line.split(" - ")

            temp_result_list.append(data)
          

    return temp_result_list
        
    
        

def main():
    low_res = extract_logs()
    mid_res = transform_logs(low_res)


if __name__ == "__main__":
    main()