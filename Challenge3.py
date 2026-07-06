import time
raw_logs = ["google.com:200", "internal-error.de:500", "testseite.com:404", "bcg.com:200"]

def ParseLogs(response,website):
    alarm_urls = []
    for log in raw_logs:
        print("Website and COde")
        sepperate = log.split(":")
        website = sepperate[0]
        response = int(sepperate[1])
        return website
        return response

def EvaluateLogs(response):
    response = ParseLogs()
    print(response)

def main():
    ParseLogs()
    EvaluateLogs()
 

if __name__ == "__main__":
     main()
