import socket

def FullWrite(fd, data):
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