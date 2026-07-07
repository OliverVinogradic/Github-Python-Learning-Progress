raw_logs = ["google.com:200", "internal-error.de:500", "testseite.com:404", "bcg.com:200"]

def ParseLogs(log_liste):
    alarm_urls = []
    for log in log_liste:
        sepperate = log.split(":")
        website = sepperate[0]
        response = int(sepperate[1])
        if response >= 400:
            alarm_urls.append(website)
            
    return alarm_urls     


def main():
    ergebnis = ParseLogs(raw_logs)
    print(ergebnis)
 

if __name__ == "__main__":
     main()
