#!/usr/bin/env python3

def crc8_common(crc, polynom):
    print("Start:", crc)
    for i in range (8):
        if (int(crc, 2) & 0x80):
            crc = bin((int(crc, 2) << 1) ^ polynom)
            print("With <<", crc)
        else:
            crc = bin(int(crc, 2) << 1)
            print("Without <<", crc)
    return crc

def crc8_oneByte(data):
    polynom = 0x1D
    crc = crc8_common(data, polynom)

    return crc[-8:]

def crc8(bytearray):
    polynom = 0x1D
    crc = 0
    for currentByte in bytearray:
        crc ^= int(currentByte, 2)
        crc8_common(bin(crc), polynom)

    return crc

print(crc8(["0b00000001", "0b00000010"]))