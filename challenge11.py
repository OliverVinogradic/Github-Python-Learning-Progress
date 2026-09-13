import os



def user_input():
    target_list = []

    while True:
        target_ip = input("Enter valid IPv4 Adresses enter stop if you want to stop\n")

        if target_ip == "stop":
                print("Collection stoped..moving to the next step\n")
                break

        else:
                print(f"[+] {target_ip} added to the list\n")
                target_list.append(target_ip)
                print("Add the next one or stop by entering stop\n")
    return target_list

def target_ping(targets):
    for target in targets:
       ping = os.system("ping -c 5 "+ target)



def main():
   user_result = user_input()
   result = target_ping(user_result)



if __name__ ==  "__main__":
    main()