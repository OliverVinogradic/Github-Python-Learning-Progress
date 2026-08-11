
def userinput():
  print(f"Hey,choose some numbers and calculate the Bin or Hex\n")
  us_input = int(input("Pick a Number\n"))
  u_choice = int(input(f"alright now choose 1.for Bin and 2. For Hex\n"))
  if u_choice > 2 or u_choice < 1 :
     print("The Choice is not listed...")
  else:
     return us_input



def calculator(u_input):

 bin_text = bin(u_input)[2:].zfill(8)





def main():
    print("Calc Starts")
    result = calculator(us_input)


if __name__ == "__main__":
    main()