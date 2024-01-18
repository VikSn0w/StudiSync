import socket
import time


def main():
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servaddr = ('127.0.0.1', 1024)

    try:
        listenfd.bind(servaddr)
        listenfd.listen(1024)
        print("Server listening on port 1024")

        while True:
            print("Waiting for connection...")
            connfd, _ = listenfd.accept()
            print("Client connected")

            ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            response = f"{ticks}\r\n"

            connfd.send(response.encode())
            connfd.close()

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        listenfd.close()


if __name__ == "__main__":
    main()
