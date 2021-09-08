import serial
import sys
import getopt
import os
import glob

ENTRIES=320000
PORT='/dev/ttyUSB1'
FILE='./'

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

#Update defaults if arguments passed in
opts, args = getopt.getopt(sys.argv[1:], 'p:P:f:F', ['PORT=','FILE='])
for opt, arg in opts:
    if   opt in ('-p', '-P', '--PORT'):  PORT = arg
    elif opt in ('-f', '-F', '--FILE'):  FILE = arg

#Capture serial Data
getSerialLogs(fileDir=FILE, comPort=PORT)

