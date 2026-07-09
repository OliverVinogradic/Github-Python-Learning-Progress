import requests

API_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_live_data(url):
    response = requests.get(url)
    live_logs = response.json()
    return live_logs

def filter_data(logs):
   critical_ids = []
   for user in logs:
      task_status = user.get("completed")
      if task_status == False:
          user_id = user.get("id")
          f_task = user.get("title")
          new_dict = {
              "User ID" : user_id,
              "Failed Task" : f_task
          }
          critical_ids.append(new_dict)

   return critical_ids



def write_report(file_name,info_file):
    temp_list = []
    with open(file_name,"w") as file:
      for critical_info in info_file:
        fail_task = critical_info.get("Failed Task")
        failed_user = critical_info.get("User ID")
        temp_list.append(fail_task)
        temp_list.append(failed_user)
   
        
        
        file.write(f"{failed_user}{fail_task}\n")
    return temp_list




def main():
    
    try:
        raw_live_data = fetch_live_data(API_URL)
    except Exception as e:
        print(f"Netzwerkfehler: {e}")
        return
    result = filter_data(raw_live_data)
    write_report("REPORT",result)
    
    
if __name__ == "__main__":
    main()