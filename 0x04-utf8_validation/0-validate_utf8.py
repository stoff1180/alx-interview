#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
     A method determine if a given data set represents a valid UTF-8 encoding
    """
    nBytes = 0

    b1 = 1 << 7
    b2 = 1 << 6

    for i in data:
        b = 1 << 7
        if nBytes == 0:
            while b & i:
                nBytes += 1
                b = b >> 1
            if nBytes == 0:
                continue
            if nBytes == 1 or nBytes > 4:
                return False
        else:
            if not (i & b1 and not (i & b2)):
                return False
        nBytes -= 1
    return nBytes == 0
