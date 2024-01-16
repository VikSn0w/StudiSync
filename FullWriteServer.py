import socket
import time

def full_write(fd, data):
    total_sent = 0
    while total_sent < len(data):
        try:
            sent = fd.send(data[total_sent:])
            if sent == 0:
                raise OSError("Socket connection broken")
            total_sent += sent
        except socket.error as e:
            if e.errno == socket.errno.EINTR:
                continue
            else:
                raise
    return total_sent

def main(ip_address):
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servaddr = (ip_address, 1024)

    try:
        listenfd.bind(servaddr)
        listenfd.listen(1024)
        print("Server listening on port 1024")

        while True:
            print("Waiting for connection...")
            connfd, _ = listenfd.accept()
            print("Client connected")

            ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            response = f"{'pisnelo'}\r\n"

            full_write(connfd, response.encode())
            connfd.close()

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        listenfd.close()

if __name__ == "__main__":
    main("127.0.0.1")
