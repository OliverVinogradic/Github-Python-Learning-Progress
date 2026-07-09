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
          critical_ids.append(user_id)

   return critical_ids

def main():
    try:
        raw_live_data = fetch_live_data(API_URL)
    except Exception as e:
        print(f"Netzwerkfehler: {e}")
        return
    result = filter_data(raw_live_data)
    print(f"Here are the IDs {result}")

if __name__ == "__main__":
    main()
