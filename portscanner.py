import socket

ip = input("Enter the IP address: ")

for port in range(1, 65525):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"Port is open:" + str(port))
        sock.close()
    else:
        print(f"Port is closed:" + str(port))
