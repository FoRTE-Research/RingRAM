DEFAULT_FPGA='VC709'

def addClock(file, FPGA=DEFAULT_FPGA):
    file.write("#Clock Source\r\n")
    if(FPGA=='VC709'):
        file.write("set_property IOSTANDARD DIFF_SSTL15 [get_ports clk_p]\r\n")
        file.write("set_property PACKAGE_PIN H19 [get_ports clk_p]\r\n")
        file.write("set_property PACKAGE_PIN G18 [get_ports clk_n]\r\n")
        file.write("set_property IOSTANDARD DIFF_SSTL15 [get_ports clk_n]\r\n")
    elif(FPGA=='A735'):
        file.write("set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports CLK]\r\n")
        file.write("create_clock -period 10.000 -name sys_clk_pin -waveform {0.000 5.000} -add [get_ports CLK]\r\n")
    elif(FPGA=='A7100'):
        file.write("set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports CLK]\r\n")
        file.write("create_clock -period 10.000 -name sys_clk_pin -waveform {0.000 5.000} -add [get_ports CLK]\r\n")
    file.write("\r\n")
    

def addLED(file, FPGA=DEFAULT_FPGA):
    file.write("#LEDs\r\n")
    if(FPGA=='VC709'):
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[7]}]\r\n")
        file.write("set_property PACKAGE_PIN AU39 [get_ports {LED[7]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[6]}]\r\n")
        file.write("set_property PACKAGE_PIN AP42 [get_ports {LED[6]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[5]}]\r\n")
        file.write("set_property PACKAGE_PIN AP41 [get_ports {LED[5]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[4]}]\r\n")
        file.write("set_property PACKAGE_PIN AR35 [get_ports {LED[4]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[3]}]\r\n")
        file.write("set_property PACKAGE_PIN AT37 [get_ports {LED[3]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[2]}]\r\n")
        file.write("set_property PACKAGE_PIN AR37 [get_ports {LED[2]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[1]}]\r\n")
        file.write("set_property PACKAGE_PIN AN39 [get_ports {LED[1]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {LED[0]}]\r\n")
        file.write("set_property PACKAGE_PIN AM39 [get_ports {LED[0]}]\r\n")
    elif(FPGA=='A735'):
        file.write("set_property -dict { PACKAGE_PIN H5    IOSTANDARD LVCMOS33 } [get_ports { LED[0] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN J5    IOSTANDARD LVCMOS33 } [get_ports { LED[1] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN T9    IOSTANDARD LVCMOS33 } [get_ports { LED[2] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN T10   IOSTANDARD LVCMOS33 } [get_ports { LED[3] }];\r\n")
    elif(FPGA=='A7100'):
        file.write("set_property -dict { PACKAGE_PIN H5    IOSTANDARD LVCMOS33 } [get_ports { LED[0] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN J5    IOSTANDARD LVCMOS33 } [get_ports { LED[1] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN T9    IOSTANDARD LVCMOS33 } [get_ports { LED[2] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN T10   IOSTANDARD LVCMOS33 } [get_ports { LED[3] }];\r\n")
    file.write("\r\n")

def addSwitches(file, FPGA=DEFAULT_FPGA):
    file.write("#Switches\r\n")
    if(FPGA=='VC709'):
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[7]}]\r\n")
        file.write("set_property PACKAGE_PIN BB31 [get_ports {SW[7]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[6]}]\r\n")
        file.write("set_property PACKAGE_PIN BA30 [get_ports {SW[6]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[5]}]\r\n")
        file.write("set_property PACKAGE_PIN AY30 [get_ports {SW[5]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[4]}]\r\n")
        file.write("set_property PACKAGE_PIN AW30 [get_ports {SW[4]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[3]}]\r\n")
        file.write("set_property PACKAGE_PIN BA32 [get_ports {SW[3]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[2]}]\r\n")
        file.write("set_property PACKAGE_PIN BA31 [get_ports {SW[2]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[1]}]\r\n")
        file.write("set_property PACKAGE_PIN AY33 [get_ports {SW[1]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {SW[0]}]\r\n")
        file.write("set_property PACKAGE_PIN AV30 [get_ports {SW[0]}]\r\n")
    elif(FPGA=='A735'):
        file.write("set_property -dict { PACKAGE_PIN A8    IOSTANDARD LVCMOS33 } [get_ports { SW[0] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN C11   IOSTANDARD LVCMOS33 } [get_ports { SW[1] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN C10   IOSTANDARD LVCMOS33 } [get_ports { SW[2] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN A10   IOSTANDARD LVCMOS33 } [get_ports { SW[3] }];\r\n")
    elif(FPGA=='A7100'):
        file.write("set_property -dict { PACKAGE_PIN A8    IOSTANDARD LVCMOS33 } [get_ports { SW[0] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN C11   IOSTANDARD LVCMOS33 } [get_ports { SW[1] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN C10   IOSTANDARD LVCMOS33 } [get_ports { SW[2] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN A10   IOSTANDARD LVCMOS33 } [get_ports { SW[3] }];\r\n")
    file.write("\r\n")

def addUART(file, FPGA=DEFAULT_FPGA):
    file.write("#Uart\r\n")
    if(FPGA=='VC709'):
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports TX]\r\n")
        file.write("set_property PACKAGE_PIN AU36 [get_ports TX]\r\n")
    elif(FPGA=='A735'):
        file.write("set_property -dict { PACKAGE_PIN D10   IOSTANDARD LVCMOS33 } [get_ports { TX }];\r\n")
        file.write("#set_property -dict {PACKAGE_PIN A9 IOSTANDARD LVCMOS33} [get_ports RX];\r\n")
    elif(FPGA=='A7100'):
        file.write("set_property -dict { PACKAGE_PIN D10   IOSTANDARD LVCMOS33 } [get_ports { TX }];\r\n")
        file.write("#set_property -dict {PACKAGE_PIN A9 IOSTANDARD LVCMOS33} [get_ports RX];\r\n")
    file.write("\r\n")

def addButtons(file, FPGA=DEFAULT_FPGA):
    file.write("#Buttons\r\n")
    if(FPGA=='VC709'):
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {BUTTON[4]}]\r\n")
        file.write("set_property PACKAGE_PIN AR40 [get_ports {BUTTON[4]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {BUTTON[3]}]\r\n")
        file.write("set_property PACKAGE_PIN AU38 [get_ports {BUTTON[3]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {BUTTON[2]}]\r\n")
        file.write("set_property PACKAGE_PIN AP40 [get_ports {BUTTON[2]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {BUTTON[1]}]\r\n")
        file.write("set_property PACKAGE_PIN AW40 [get_ports {BUTTON[1]}]\r\n")
        file.write("set_property IOSTANDARD LVCMOS18 [get_ports {BUTTON[0]}]\r\n")
        file.write("set_property PACKAGE_PIN AV39 [get_ports {BUTTON[0]}]\r\n")
    elif(FPGA=='A735'):
        file.write("set_property -dict { PACKAGE_PIN D9    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[0] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN C9    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[1] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN B9    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[2] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN B8    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[3] }];\r\n")
    elif(FPGA=='A7100'):
        file.write("set_property -dict { PACKAGE_PIN D9    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[0] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN C9    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[1] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN B9    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[2] }];\r\n")
        file.write("set_property -dict { PACKAGE_PIN B8    IOSTANDARD LVCMOS33 } [get_ports { BUTTON[3] }];\r\n")
    file.write("\r\n")

def addClockBlock(file, FPGA=DEFAULT_FPGA):
    file.write("create_pblock pblock_clk_div\r\n")
    file.write("add_cells_to_pblock [get_pblocks pblock_clk_div] [get_cells -quiet [list clk_div]]\r\n")

    if(FPGA=='VC709'):
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {SLICE_X196Y475:SLICE_X221Y499}\r\n")
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {RAMB18_X13Y190:RAMB18_X14Y199}\r\n")
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {RAMB36_X13Y95:RAMB36_X14Y99}\r\n")
    elif(FPGA=='A735'):
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {SLICE_X36Y134:SLICE_X57Y149}\r\n")
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {RAMB18_X1Y54:RAMB18_X1Y59}\r\n")
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {RAMB36_X1Y27:RAMB36_X1Y29}\r\n")
        file.write("set_property BEL MMCME2_ADV [get_cells clk_div/MMCME2_ADV_inst]\r\n")
        file.write("set_property LOC MMCME2_ADV_X1Y1 [get_cells clk_div/MMCME2_ADV_inst]\r\n")
    elif(FPGA=='A7100'):
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {SLICE_X66Y134:SLICE_X79Y149}\r\n")
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {RAMB18_X2Y54:RAMB18_X2Y59}\r\n")
        file.write("resize_pblock [get_pblocks pblock_clk_div] -add {RAMB36_X2Y27:RAMB36_X2Y29}\r\n")
        file.write("set_property BEL MMCME2_ADV [get_cells clk_div/MMCME2_ADV_inst]\r\n")
        file.write("set_property LOC MMCME2_ADV_X1Y1 [get_cells clk_div/MMCME2_ADV_inst]\r\n")


    file.write("set_property SNAPPING_MODE ON [get_pblocks pblock_clk_div]\r\n")
    file.write("\r\n")

def addUARTCtrlBlock(file, FPGA=DEFAULT_FPGA):
    file.write("create_pblock pblock_uart_ctrl\r\n")
    file.write("add_cells_to_pblock [get_pblocks pblock_uart_ctrl] [get_cells -quiet [list uart_ctrl]]\r\n")

    if(FPGA=='VC709'):
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {SLICE_X170Y475:SLICE_X195Y499}\r\n")
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {RAMB18_X11Y190:RAMB18_X12Y199}\r\n")
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {RAMB36_X11Y95:RAMB36_X12Y99}\r\n")
    elif(FPGA=='A735'):
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {SLICE_X36Y118:SLICE_X57Y133}\r\n")
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {RAMB18_X1Y50:RAMB18_X1Y51}\r\n")
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {RAMB36_X1Y25:RAMB36_X1Y25}\r\n")
    elif(FPGA=='A7100'):
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {SLICE_X52Y134:SLICE_X65Y149}\r\n")
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {RAMB18_X1Y54:RAMB18_X1Y59}\r\n")
        file.write("resize_pblock [get_pblocks pblock_uart_ctrl] -add {RAMB36_X1Y27:RAMB36_X1Y29}\r\n")

    file.write("set_property SNAPPING_MODE ON [get_pblocks pblock_uart_ctrl]\r\n")
    file.write("\r\n")

def addRRAMCtrlBlock(file, FPGA=DEFAULT_FPGA):
    file.write("create_pblock pblock_rram_ctrl\r\n")
    file.write("add_cells_to_pblock [get_pblocks pblock_rram_ctrl] [get_cells -quiet [list rram_ctrl instdb]]\r\n")

    if(FPGA=='VC709'):
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {SLICE_X170Y0:SLICE_X221Y474}\r\n")
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {RAMB18_X11Y0:RAMB18_X14Y189}\r\n")
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {RAMB36_X11Y0:RAMB36_X14Y94}\r\n")
    elif(FPGA=='A735'):
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {SLICE_X36Y0:SLICE_X65Y99}\r\n")
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {RAMB18_X1Y0:RAMB18_X2Y39}\r\n")
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {RAMB36_X1Y0:RAMB36_X2Y19}\r\n")
    elif(FPGA=='A7100'):
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {SLICE_X52Y0:SLICE_X79Y133}\r\n")
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {RAMB18_X1Y0:RAMB18_X2Y51}\r\n")
        file.write("resize_pblock [get_pblocks pblock_rram_ctrl] -add {RAMB36_X1Y0:RAMB36_X2Y25}\r\n")

    file.write("set_property SNAPPING_MODE ON [get_pblocks pblock_rram_ctrl]\r\n")
    file.write("\r\n")

