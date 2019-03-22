#!/usr/bin/env python3

def crc8_common(crc, polynom):
    for i in range (8):
        if (int(crc, 2) & 0x80):
            crc = bin((int(crc, 2) << 1) ^ polynom)
        else:
            crc = bin(int(crc, 2) << 1)
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

    return bin(crc)[-8:]

print(crc8(["0b00000001", "0b00000010"]))