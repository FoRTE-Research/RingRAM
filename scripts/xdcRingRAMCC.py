import sys
import getopt
import os
import xdcAddBlocks as xdc

FPGA='A7100'

#Set Default Values
if   (FPGA=='A7100'): N_CELLS=64; N_INV=5; POS_X=38; POS_Y=128;
elif (FPGA=='A735'):  N_CELLS=50; N_INV=5; POS_X=16; POS_Y=100;
elif (FPGA=='VC709'): N_CELLS=64; N_INV=5; POS_X=78; POS_Y=300;
RRAM_PATH='rram_ctrl/rram'
FILE_PATH=''

#Update defaults if arguments passed in
opts, args = getopt.getopt(sys.argv[1:], 'f:F:c:C:i:I:x:X:y:Y:p:P:l:L:', ['FPGA=', 'CELLS=', 'INV=', 'POSX=', 'POSY=', 'PATH=', 'LOC='])
for opt, arg in opts:
    if   opt in ('-f', '-F', '--FPGA'):  FPGA      = arg
    elif opt in ('-c', '-C', '--Cells'): N_CELLS   = int(arg)
    elif opt in ('-i', '-I', '--INV'):   N_INV     = int(arg)
    elif opt in ('-x', '-X', '--POSX'):  POS_X     = int(arg)
    elif opt in ('-y', '-Y', '--POSY'):  POS_Y     = int(arg)
    elif opt in ('-p', '-P', '--PATH'):  FILE_PATH = arg
    elif opt in ('-l', '-L', '--LOC'):   RRAM_PATH = arg

#Set file path if not set
if(FILE_PATH==''): FILE_PATH='./top_level_'+FPGA+'.xdc'
print(FILE_PATH)

#Assign Lut locations based on inverter size
if  (N_INV==1): LUTLOC=['D5', 'A6']
elif(N_INV==3): LUTLOC=['D6', 'A5', 'D5', 'A6']
elif(N_INV==5): LUTLOC=['B6', 'C6', 'D6', 'B5', 'D5', 'A6']
elif(N_INV==7): LUTLOC=['B6', 'C6', 'D6', 'A5', 'B5', 'C5', 'D5', 'A6']

#Remove Previous file
if os.path.exists(FILE_PATH):
  os.remove(FILE_PATH)
          
#Create New File
file = open(FILE_PATH, mode='w')

#Add Board pinouts
xdc.addClock(file, FPGA)
xdc.addUART(file, FPGA)
xdc.addButtons(file, FPGA)

#Add pblocks
xdc.addClockBlock(file, FPGA)
xdc.addUARTCtrlBlock(file, FPGA)
xdc.addRRAMCtrlBlock(file, FPGA)

#Add RingRAM place/route
for INDEX_CELL in range(0, round(N_CELLS), 1):
    #Suppress Combinational Loop Warning
    file.write('set_property ALLOW_COMBINATORIAL_LOOPS true [get_nets {%s/genblk1[%d].genblk1[%d].g_inv_buff_1/o}]\r\n' % (RRAM_PATH, INDEX_CELL, 0)) #Suppress Warning

    #Position - NAND Gates
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s/genblk1[%d].g_and_%d/o_INST_0}]\r\n'  % (POS_X, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property BEL %sLUT        \t[get_cells {%s/genblk1[%d].g_and_%d/o_INST_0}]\r\n'  % ('A6', RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s/genblk1[%d].g_and_%d/o_INST_0}]\r\n'  % (POS_X+8, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 2))
    file.write('set_property BEL %sLUT        \t[get_cells {%s/genblk1[%d].g_and_%d/o_INST_0}]\r\n'  % ('A6', RRAM_PATH, INDEX_CELL, 2))

    for INV_INDEX in range(0, N_INV, 1):
        file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s/genblk1[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (POS_X, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, INV_INDEX, 1))
        file.write('set_property BEL %sLUT        \t[get_cells {%s/genblk1[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (LUTLOC[INV_INDEX], RRAM_PATH, INDEX_CELL, INV_INDEX, 1))
        file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s/genblk1[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (POS_X+8, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, INV_INDEX, 2))
        file.write('set_property BEL %sLUT        \t[get_cells {%s/genblk1[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (LUTLOC[INV_INDEX], RRAM_PATH, INDEX_CELL, INV_INDEX, 2))

    #Position - Output Buffers
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s/genblk1[%d].g_out_buff_%d}]\r\n' % (POS_X+1, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property BEL %sLUT        \t[get_cells {%s/genblk1[%d].g_out_buff_%d}]\r\n' % (LUTLOC[N_INV], RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s/genblk1[%d].g_out_buff_%d}]\r\n' % (POS_X+1+8, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 2))
    file.write('set_property BEL %sLUT        \t[get_cells {%s/genblk1[%d].g_out_buff_%d}]\r\n' % (LUTLOC[N_INV], RRAM_PATH, INDEX_CELL, 2))

    #Position - Enable Buffers
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s/genblk1[%d].g_en_buff}]\r\n' % (POS_X+4, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL))
    file.write('set_property BEL %sLUT        \t[get_cells {%s/genblk1[%d].g_en_buff}]\r\n' % ('A6', RRAM_PATH, INDEX_CELL))

#Close File
file.close()

