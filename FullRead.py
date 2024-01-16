import os
import sys
import errno


def FullRead(fd, buf, count):
    nleft = count
    while nleft > 0:
        try:
            nread = os.read(fd, min(nleft, len(buf)))
        except OSError as e:
            if e.errno == errno.EINTR:
                continue
            else:
                sys.exit(e.errno)

        if not nread:  # EOF
            break

        nleft -= nread
        buf[:nread] = bytes(nread)  # Assuming buf is a bytearray or similar mutable buffer

    return nleft
