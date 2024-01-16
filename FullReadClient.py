import socket
import sys

def full_read(fd, count):
    data = b""
    while count > 0:
        try:
            chunk = fd.recv(count)
            if not chunk:
                break
            data += chunk
            count -= len(chunk)
        except socket.error as e:
            if e.errno == socket.errno.EINTR:
                continue
            else:
                raise
    return data

def main(ip_address):


    ip_address = ip_address
    port = 1024

    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servaddr = (ip_address, port)

    try:
        sockfd.connect(servaddr)
        print(f"Connected to {ip_address}:{port}")

        recvline = full_read(sockfd, 1024)

        if sys.stdout.buffer.write(recvline) == -1:
            sys.stderr.write("fputs error\n")
            sys.exit(1)

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sockfd.close()

if __name__ == "__main__":
    main("127.0.0.1")
