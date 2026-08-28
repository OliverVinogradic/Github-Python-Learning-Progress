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

    http_request = "HEAD / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n"
    s.send(http_request.encode('utf-8'))

    banner = s.recv(1024).decode('utf-8', errors='ignore')
    
    print("\n--- Recieved BANNER ---")
    print(banner)
    print("--------------------------")
    
except Exception as e:
    print(f"[-] Error {e}")