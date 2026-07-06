import time

Ports = []






def CheckSicherheitsRisiko(offene_ports):
    if offene_ports > 10:
      print(f"Port {offene_ports}  ist offen sofot schließen!\n")
     
    
    elif offene_ports > 0:
      print(f"Port {offene_ports} ist offen bitte schließen!\n")
     

    elif offene_ports == 0:
       print(f"Port {offene_ports} ist offen sicher!")

    

def PortinListe():
  for i in range(5):
    Port = int(input("Welcher Port ist offen?\n"))
    time.sleep(1)
    Ports.append(Port)

def listeauflösen():
  for Port in Ports:
    Outcome = CheckSicherheitsRisiko(Port)
  
def main():
  PortinListe()
  listeauflösen()
  

if __name__ == "__main__":
    main()
