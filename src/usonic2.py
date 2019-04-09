#!/usr/bin/env python3

import serial
import time

if __name__ == "__main__":

    port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    i = 0
    while True:
        i += 1
        print(i)
        time.sleep(0.1)
