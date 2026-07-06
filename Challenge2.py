import time
CWebsites = "CostumerWebsites.txt"
Websites = []


#print the Websites
def printWebsites():
   for Website in Websites:
      print(Website)

#Get the websites from the txt file and adds them into the Website list
def LoadeWebsites():
  try:
    with open(CWebsites,"r",encoding="utf-8")as f:
      for zeile in f:
        url = zeile.strip() 
        Websites.append(url)
  except FileNotFoundError:
     print("File not found")

#just loads the functions
def main():
  LoadeWebsites()
  printWebsites()

if __name__ == "__main__":
     main()