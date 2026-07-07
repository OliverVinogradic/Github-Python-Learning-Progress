ClientWeb = "KundenWebsites.txt"

def LadeUndParseLogs():
    fehlerhafte_seiten = []
    try:
        with open(ClientWeb, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue
                sepperate = line.split(":")
                code = int(sepperate[1])
                
                if code >= 400:
                    website = sepperate[0]
                    fehlerhafte_seiten.append(website) 
                    
        return fehlerhafte_seiten
                                    
    except FileNotFoundError:
        print("File not found")
        return [] 
def main():
    ergebnis = LadeUndParseLogs()
    print(ergebnis) 

if __name__ == "__main__":
    main()