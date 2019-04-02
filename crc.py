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

# print(crc8_oneByte("0b11000010"))

def crc8(bytearray):
    polynom = 0x1D
    crc = 0
    for currentByte in bytearray:
        crc = crc ^ currentByte
        crc = int(crc8_common(bin(crc), polynom), 2)

    return bin(crc)[-8:]

# print(crc8(bytearray([1, 2])))


