import serial
import sys
import getopt
import os
import glob

ENTRIES=320000
PORT='/dev/ttyUSB1'
FILE='./data/SerialLog'

PRIMITIVE='RRAM\r\n'

def getSerialLogs(filePath='./data/SerialLog', comPort='/dev/ttyUSB1', baudRate=115200):
    
    #Extract File Dir
    fileDir=os.path.dirname(os.path.abspath(filePath))
    
    #If Dir does not exist
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)

    #If file already exists
    if os.path.exists(filePath):
      os.remove(filePath)
      
    print(filePath)

    #Serial setup
    ser = serial.Serial(comPort, baudRate, xonxoff=False, timeout=1)

    #Write serial input to file
    with open(filePath, 'a') as f:
        
        #Wait for header
        serial_in = ser.readline()
        while serial_in != PRIMITIVE.encode('UTF-8'):
            serial_in = ser.readline()
        f.write(PRIMITIVE)
        f.flush()
        
        serialByte={}
        #Capture Data
        for i in range(0, ENTRIES, 1):
            serialByte = ser.read(16)
            serialBin = ''.join([bin(i)[2:].zfill(8) for i in list(serialByte)])

            if(PRIMITIVE=='RO  \r\n'):
                f.write(serialBin[ 0: 64]+"\r\n")
                f.write(serialBin[64:128]+"\r\n")
            elif(PRIMITIVE=='RRAM\r\n'):
                f.write(serialBin[64:128]+"\r\n")
                if(serialBin[0:64]!="1111111111111111111111111111111111111111111111111111111111111111"):
                    print("ENABLE LOW FAIL - line %d - Check %s Output %s" % (i, serialBin[0:64], serialBin[64:128]))
            f.flush()

        #Close objects
        ser.close()
        f.close()

#Update defaults if arguments passed in
opts, args = getopt.getopt(sys.argv[1:], 'p:P:f:F:', ['PORT=','FILE='])
for opt, arg in opts:
    if   opt in ('-p', '-P', '--PORT'):  PORT = arg
    elif opt in ('-f', '-F', '--FILE'):  FILE = arg

#Capture serial Data
getSerialLogs(filePath=FILE, comPort=PORT)


