import socket
import sys

def main(client_ip, server_ip):
    '''
        if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <IPaddress>")
        sys.exit(1)
    '''
    ip_address = server_ip
    port = 5000
    recv_size = 1024

    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servaddr = (ip_address, port)

    try:
        sockfd.connect(servaddr)
        print(f"Connected to {ip_address}:{port}")

        while True:
            data = sockfd.recv(recv_size)
            if not data:
                break
            print(data.decode(), end='')

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sockfd.close()

if __name__ == "__main__":
    main("127.0.0.1","127.0.0.1")
