import os
import sys
import errno

def FullWrite(fd, buf, count):
    nleft = count
    while nleft > 0:
        try:
            nwritten = os.write(fd, buf[:nleft])
        except OSError as e:
            if e.errno == errno.EINTR:
                continue
            else:
                sys.exit(e.errno)
        nleft -= nwritten
        buf = buf[nwritten:]
    return nleft

# Note: In Python, there is no direct equivalent to file descriptors as in C,
# so you'll need to use file objects or use the `os` module for low-level I/O operations.
# The `os.write` function is similar to the `write` system call in C.
