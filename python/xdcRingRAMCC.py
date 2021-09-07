import sys
import os
import xdcAddBlocks as xdc

FPGA='A7100'

#Set Default Values
if   (FPGA=='A7100'): N_CELLS=64; N_INV=5; POS_X=38; POS_Y=128;
elif (FPGA=='A735'):  N_CELLS=50; N_INV=5; POS_X=16; POS_Y=100;
elif (FPGA=='VC709'): N_CELLS=64; N_INV=5; POS_X=78; POS_Y=300;

#Update defaults if arguments passed in
if len(sys.argv) > 1 : FPGA    = sys.argv[1]
if len(sys.argv) > 2 : N_CELLS = int(sys.argv[2])
if len(sys.argv) > 3 : N_INV   = int(sys.argv[3])
if len(sys.argv) > 4 : POS_X   = int(sys.argv[4])
if len(sys.argv) > 5 : POS_Y   = int(sys.argv[5])

#Set paths
file_name='./top_level_'+FPGA+'.xdc'
RRAM_PATH='rram_ctrl/rram/genblk1'

#Assign Lut locations based on inverter size
if  (N_INV==1): LUTLOC=['D5', 'A6']
elif(N_INV==3): LUTLOC=['D6', 'A5', 'D5', 'A6']
elif(N_INV==5): LUTLOC=['B6', 'C6', 'D6', 'B5', 'D5', 'A6']
elif(N_INV==7): LUTLOC=['B6', 'C6', 'D6', 'A5', 'B5', 'C5', 'D5', 'A6']

#Remove Previous file
if os.path.exists(file_name):
  os.remove(file_name)
          
#Create New File
file = open(file_name, mode='w')

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
    file.write('set_property ALLOW_COMBINATORIAL_LOOPS true [get_nets {%s[%d].genblk1[%d].g_inv_buff_1/o}]\r\n' % (RRAM_PATH, INDEX_CELL, 0)) #Suppress Warning

    #Position - NAND Gates
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s[%d].g_and_%d/o_INST_0}]\r\n'  % (POS_X, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property BEL %sLUT        \t[get_cells {%s[%d].g_and_%d/o_INST_0}]\r\n'  % ('A6', RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s[%d].g_and_%d/o_INST_0}]\r\n'  % (POS_X+8, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 2))
    file.write('set_property BEL %sLUT        \t[get_cells {%s[%d].g_and_%d/o_INST_0}]\r\n'  % ('A6', RRAM_PATH, INDEX_CELL, 2))

    for INV_INDEX in range(0, N_INV, 1):
        file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (POS_X, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, INV_INDEX, 1))
        file.write('set_property BEL %sLUT        \t[get_cells {%s[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (LUTLOC[INV_INDEX], RRAM_PATH, INDEX_CELL, INV_INDEX, 1))
        file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (POS_X+8, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, INV_INDEX, 2))
        file.write('set_property BEL %sLUT        \t[get_cells {%s[%d].genblk1[%d].g_inv_buff_%d/o_INST_0}]\r\n' % (LUTLOC[INV_INDEX], RRAM_PATH, INDEX_CELL, INV_INDEX, 2))

    #Position - Output Buffers
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s[%d].g_out_buff_%d}]\r\n' % (POS_X+1, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property BEL %sLUT        \t[get_cells {%s[%d].g_out_buff_%d}]\r\n' % (LUTLOC[N_INV], RRAM_PATH, INDEX_CELL, 1))
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s[%d].g_out_buff_%d}]\r\n' % (POS_X+1+8, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL, 2))
    file.write('set_property BEL %sLUT        \t[get_cells {%s[%d].g_out_buff_%d}]\r\n' % (LUTLOC[N_INV], RRAM_PATH, INDEX_CELL, 2))

    #Position - Enable Buffers
    file.write('set_property LOC SLICE_X%dY%d \t[get_cells {%s[%d].g_en_buff}]\r\n' % (POS_X+4, POS_Y+INDEX_CELL, RRAM_PATH, INDEX_CELL))
    file.write('set_property BEL %sLUT        \t[get_cells {%s[%d].g_en_buff}]\r\n' % ('A6', RRAM_PATH, INDEX_CELL))

#Close File
file.close()

