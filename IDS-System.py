import time




def transform_logs(temp_result_list):
     all_dics = []

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
    
        all_dics.append(temp_dict)
     return all_dics

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


def analyse_logs(data_dictonary):
    for data in data_dictonary:
        status_code = data.get(int("Status Code"))
        if status_code == 401:
            print(status_code)
        else:
            print("No error")


        
    
        

def main():
    low_res = extract_logs()
    mid_res = transform_logs(low_res)
    print(mid_res)
    end_res = analyse_logs(mid_res)


if __name__ == "__main__":
    main()