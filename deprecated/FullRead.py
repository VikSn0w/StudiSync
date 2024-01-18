import socket

def FullRead(fd, count):
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