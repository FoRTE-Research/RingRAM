VIVADO_CMD= vivado

default:
	@echo "RingRAM-A735 : create a vivado project for the Arty-A735  evaluation"
	@echo "RingRAM-A7100: create a vivado project for the Arty-A7100 evaluation"
	@echo "RingRAM-VC709: create a vivado project for the Virtex7-VC709 evaluation"
	@echo "clean: Remove all generated files"

RingRAM-A735:
	$(VIVADO_CMD) -mode batch -nolog -nojournal -source ./tcl/RingRAM.tcl -tclargs RingRAM_A735 ./vivado/RingRAM_A735/ xc7a35ticsg324-1L digilentinc.com:arty-a7-35:part0:1.0 ./HDL/top_level_A735.v ./HDL/top_level_A735.xdc

RingRAM-A7100:
	$(VIVADO_CMD) -mode batch -nolog -nojournal -source ./tcl/RingRAM.tcl -tclargs RingRAM_A7100 ./vivado/RingRAM_A7100/ xc7a100tcsg324-1 digilentinc.com:arty-a7-100:part0:1.0 ./HDL/top_level_A7100.v ./HDL/top_level_A7100.xdc

RingRAM-VC709:
	$(VIVADO_CMD) -mode batch -nolog -nojournal -source ./tcl/RingRAM.tcl -tclargs RingRAM_VC709 ./vivado/RingRAM_VC709/ xc7vx690tffg1761-2 xilinx.com:vc709:part0:1.8 ./HDL/top_level_VC709.v ./HDL/top_level_VC709.xdc

clean:
	rm -rf .Xil
	rm -rf vivado


