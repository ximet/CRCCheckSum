#!/usr/bin/env python3

def crc8_common(crc, polynom):
    for i in range (8):
        if (int(crc, 2) & 0x80):
            crc = bin((int(crc, 2) << 1) ^ polynom);
            print("With <<", crc);
        else:
            crc = bin(int(crc, 2) << 1);
            print("Without <<", crc);
    return crc;

def crc8_oneByte(data):
    polynom = 0x1D;
    crc = crc8_common(data, polynom);

    return crc[-8:]

print(crc8_oneByte("0b11000010"))