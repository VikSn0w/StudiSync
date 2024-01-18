import sys
import socket
from FullWrite import FullWrite
from FullRead import FullRead

def main(ip_address):


    ip_address = ip_address
    port = 1024

    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servaddr = (ip_address, port)

    try:
        sockfd.connect(servaddr)
        print(f"Connected to {ip_address}:{port}")

        request = "read"
        FullWrite(sockfd, request.encode())
        recvline = FullRead(sockfd, 1024)

        if sys.stdout.buffer.write(recvline) == -1:
            sys.stderr.write("fputs error\n")
            sys.exit(1)

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sockfd.close()

if __name__ == "__main__":
    main("127.0.0.1")
