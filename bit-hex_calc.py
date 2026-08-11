
def userinput():
  print(f"Hey,choose some numbers and calculate the Bin or Hex\n")

  us_input = int(input("Pick a Number\n"))
  us_choice = int(input(f"alright now choose 1.for Bin and 2. For Hex\n"))

  if us_choice > 2 or us_choice < 1 :
     print("The Choice is not listed...")
     return userinput()
  else:
     return us_input,us_choice



def calculator(u_input,u_choice):
  if u_choice == 1:
   bin_text = bin(u_input)[2:].zfill(8)
   return bin_text
  else:
   hex_text = hex(u_input)[2:].upper().zfill(2)
   return hex_text







def main():
    print("Calc Starts")
    u_result,u_choice = userinput()
    result = calculator(u_result,u_choice)
    print(result)


if __name__ == "__main__":
     main()