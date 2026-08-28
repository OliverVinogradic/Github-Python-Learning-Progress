import socket

s_target = "scanme.nmap.org"
s_port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((s_target,s_port))
    if result == 0:
        print(f"[+]  Connecting to target {s_target} was Succesfull!")
    else:
        print(f"[-] Connection to {s_target} failed!")



except Exception as e:
    print(f"[-] Error {e}")