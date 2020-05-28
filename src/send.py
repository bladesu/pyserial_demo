'''
This script is used to write certain strings alternatively to a connected com port.
ref: https://pyserial.readthedocs.io/en/latest/shortintro.html
'''
import serial
import os.path
import time

# Initialization of Serial object.
# TODO hard code device location
alt_time = 1
dev = '/dev/tty.wchusbserial14130'
retry = 1
retryLmt = 10
while True:
    if (os.path.exists(dev)):
        print("Found dev:%s, load it:" % (dev))
        ser = serial.Serial(port=dev, baudrate=9600)
        break
    else:
        print("dev %s not found, retry: %d" %(dev, retry))
    retry = retry + 1
    if (retry > retryLmt):
        exit(1)

data1 = b'20'
data2 = b'21'
while (True):
    try:
        for data in [data1, data2]:
            print("send data:", data)
            ser.write(data)
            ser.flush()
            time.sleep(alt_time)
    except KeyboardInterrupt:
        print('Stop by KeyboardInterrupt')
        break
ser.close()

exit(0)