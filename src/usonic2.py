#!/usr/bin/env python3

import serial
import time
import random

if __name__ == "__main__":

    random.seed()

    port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    i = 0
    while True:
        i += 1
        iu = random.randint(-6000,6000)
        iv = random.randint(-6000,6000)
        it = random.randint( -100,3000)
        iq = random.randint(   90, 100)
        data_line = "M:x = %5d y = %5d t = %5d q = %5d\n" % (iu, iv, it, iq)
        print(data_line[:-1])
        data      = bytearray()
        data.extend(map(ord, data_line))
        port.write(data)
        time.sleep(0.1)
