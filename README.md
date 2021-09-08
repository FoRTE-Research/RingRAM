# RingRAM

RingRAM is a single hardware security primitive composed of basic circuit elements that harnesses both manufacturing and operational chaos to serve as the foundation for both a true random-number generator (TRNG) and a physical unclonable function (PUF) suitable for deployment in resource-constrained Internet-of-Things (IoT) devices.

This repository contains artifacts to enable reviewers to reproduce the experiments/results describe in "RingRAM: A Unified Hardware Security Primitive for IoT Devices that Gets Better with Age"

## Prerequisites
Software required to execute included demos:
1. [Vivado Design Suit](https://www.xilinx.com/support/download.html): Synthesising and Implementing RingRAM on included evaluation boards
2. [python3](https://www.python.org/downloads/): Required for capturing data and customing place/route
3. make: Run build scripts

## Evaluation Boards
Evaluation Boards included in this demo
1. [Arty A7-35](https://www.xilinx.com/products/boards-and-kits/1-elhaap.html)
2. [Arty A7-100](https://www.xilinx.com/products/boards-and-kits/1-w51quh.html)
3. [VC709](https://www.xilinx.com/products/boards-and-kits/dk-v7-vc709-g.html)

## Installation

Clone RingRAM repository
```
git clone git@github.com:FoRTE-Research/RingRAM.git
cd RingRAM
```
Creating vivado project using ```make``` commands:
1. Arty A7-35: ```make RingRAM-A735```
2. Arty A7-100: ```make RingRAM-A7100```
3. Virtex 7-VC709: ```make RingRAM-VC709```

Creating vivado project manually:
1. Open Vivado
2. Create Project
3. Name Project
4. Project Type - RTL Project
5. Add Sources - Include Verilog (.v) files in HDL directory
6. Add Constraints - Include Xilinx Design Constraints (.xdc) files in HDL directory

## Evaluation
To evaluate the 

### Evaluation Block Diagram
<p align="center">
	<img src="/fig/RRAM_eval_block.png" />
</p>

1. Debouncer -- Debounces the reset button
2. Clock Divider -- Utilizes a MMCM to divide the source clock to a 10MHz clock
3. RingRAM Controller -- State Machine that controls and transmits the state of the RingRAM primitive
4. Uart Controller -- Transmits the current state of 

### Evaluation State Machine
<p align="center">
	<img src="/fig/RRAM_eval_SM.png" />
</p>

1. Low/High Enable -- Iterate through each RingRAM cell setting their enables. Low enables prevent any feedback and reset the race condition.
2. Low/High Wait -- Wait time between each reset
3. Low/High Write -- Snapshot the output state of each RingRAM cell
4. Low/High Serial -- Transmite RingRAM cell snapshot
5. Low/High Serial Wait -- Wait for serial to finish transmission

## Customizations
There are two sources of variation that a designer must avoid when implementing RingRAM: systematic and structural. Systematic variation occurs both at manufacturing- and run-time. Systematic variation occurs due to predictable changes in transistor properties at chip- and wafer-scale and due to long-running changes in a device’s operational environment. We provide two guidelines to avoid these sources of variation:
1. **Symmetric**: As both components and wires have the potential to add structural variation, use symmetrical placement and routing to avoid structural variation.
2. **Tightly-packed**: By keeping the chains of a cell physically adjacent and its routing short, there is little room for systematic variation to influence chains asymmetrically.

The ```xdcRingRAMCC``` script generates a Xilinx Design Constraints (.xdc) file that adheres to these guidelines.

Command:
```
python3 ./scripts/xdcRingRAMCC [-F] [-C] [-I] [-X] [-Y] [-P]
```
Parameters:
1. ```[-f] [-F] [--FPGA]```: Which FPGA design to use (A7100, A735, VC709)
2. ```[-c] [-C] [--CELLS]```: How many RingRAM cells to generate
3. ```[-i] [-I] [--INV]```: Length of the RingRAM inverter chain (1,3,5,7)
4. ```[-x] [-X] [--POSX]```: Starting horizontal index of the FPGA LUT
5. ```[-y] [-Y] [--POSY]```: Starting vertical index of the FPGA LUT
6. ```[-p] [-P] [--PATH]```: The location and name of the RingRAM primitive

### Placement
To customize the physical location of the RingRAM cells modify the ```[-X]``` and ```[-Y]``` parameters. However, as it is important to keep symmetry, you should examine the LUT placements of the FPGA. Open the synthesis/implementation design in Vivado and examine the layout to determine which cells to use.

### Inverter Chain Length
To customize the inverter chain length of the RingRAM cells modify the:
1. ```./scripts/xdcRingRAMCC```: The```[-I]``` parameter
2. ```./HDL/top_level```: The ``` g_RRAM_INV``` parameter

### RingRAM Cells
To customize the number of RingRAM cells modify the:
1. ```./scripts/xdcRingRAMCC```: The```[-C]``` parameter
2. ```./HDL/top_level```: The ``` g_RRAM_CELLS``` parameter

### Porting to another FPGA
The RingRAM primitive ```./HDL/RRAM.v``` can be instantiated in any design or on any FPGA. To customize the number of cells or the length of the inverter chains set the ``` g_RRAM_CELLS``` or ``` g_RRAM_INV``` parameters respectively.

However to port the RingRAM layout it is necessary to modify the:
1.  ```./scripts/xdcRingRAMCC```: ```[-P]``` parameter
2. ```./scripts/xdcAddBlocks```: add blocks to contain the equivalent pinouts and pblock locations.
