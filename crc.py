#!/usr/bin/env python3
def crc(data):
    polynom = 0x1D;
    crc = data;
    for i in range (8):
        if (crc & 0x80):
            crc = ((crc << 1) ^ polynom);
        else:
            crc <<= 1;
    return bin(crc)


print(crc(0xC2))