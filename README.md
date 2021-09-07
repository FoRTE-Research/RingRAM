# RingRAM

RingRAM is a single hardware security primitive composed of basic circuit elements that harnesses both manufacturing and operational chaos to serve as the foundation for both a true random-number generator (TRNG) and a physical unclonable function (PUF) suitable for deployment in resource-constrained Internet-of-Things (IoT) devices.

This repository contains artifacts to enable reviewers to reprodude the experiments/results describe in "RingRAM: A Unified Hardware Security Primitive for IoT Devices that Gets Better with Age"

## Prerequisites
Software required to execute included demos:
1. [Vivado Design Suit](https://www.xilinx.com/support/download.html): Synthesising and Implementing RingRAM on included evaluation boards
2. python3: Required for capturing data and customing place/route
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
3. RingRAM Controller -- State Machine that controlles and transmits the state of the RingRAM primitive
4. Uart Controller -- Transmits the current state of 

### Evaluation State Machine
<p align="center">
	<img src="/fig/RRAM_eval_SM.png" />
</p>

1. Low/High Enable -- Iterate through each RingRAM cell setting their enables. Low enables prevent any feedback and reset the race condition.
2. Low/High Wait -- Wait time between each reset
3. Low/High Write -- Snapshot the output state of each RingRAM cell
4. Low/High Serial -- Transmite RingRAM cell snapshot
5. Low/High Serial Wait -- Wait for serial to finish transmition

## Modifications


### Placement

### Inverter Chain Length

### Porting to another FPGAs

