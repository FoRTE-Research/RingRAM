import serial
import sys
import os
import glob

ENTRIES=320000


def getSerialLogs(fileDir='../data/', fileName='RRAMLog', comPort='/dev/ttyUSB1', baudRate=115200):
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)

    #Remove previous file
    if os.path.exists(fileDir+fileName):
      os.remove(fileDir+fileName)

    #Serial setup
    ser = serial.Serial(comPort, baudRate, xonxoff=False, timeout=1)

    #Write serial input to file
    with open(fileDir+fileName, 'a') as f:
        
        #Wait for header
        serial_in = ser.readline()
        while serial_in != b'RRAM\r\n':
            serial_in = ser.readline()
        f.write("RRAM\r\n")
        
        serialByte={}
        #Capture Data
        for i in range(0, ENTRIES, 1):
            serialByte = ser.read(16)
            serialBin = ''.join([bin(i)[2:].zfill(8) for i in list(serialByte)])
            f.write(serialBin[64:128]+"\r\n")
            if(serialBin[0:64]!="1111111111111111111111111111111111111111111111111111111111111111"):
                print("ENABLE LOW FAIL - line %d - Check %s Output %s" % (i, serialBin[0:64], serialBin[64:128]))

        #Close objects
        ser.close()
        f.close()

if len(sys.argv) > 1 : PORT = sys.argv[1]
else                 : PORT='/dev/ttyUSB1'

getSerialLogs(fileDir='./', comPort=PORT)

