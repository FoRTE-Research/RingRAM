set pName     [lindex $argv 0]
set pPath     [lindex $argv 1]
set fpgaPart  [lindex $argv 2]
set boardPart [lindex $argv 3]
set topPath   [lindex $argv 4]
set xdcPath   [lindex $argv 5]

#Create Project
create_project [list ${pName}] [list ${pPath}] -part [list ${fpgaPart}] -force
set_property board_part [list ${boardPart}] [current_project]
add_files -norecurse [list ./HDL/CLK_DIV.v ./HDL/DEBOUNCER.v ./HDL/UART_CTRL.v ./HDL/UART_TX.vhd ./HDL/RRAM_CTRL.v ./HDL/RRAM.v ./HDL/my_and.v ./HDL/my_nand.v ./HDL/my_not.v ${topPath} ]

import_files -force -norecurse
import_files -fileset constrs_1 -force -norecurse [list ${xdcPath}]

set_property top top_level [current_fileset]
update_compile_order -fileset sources_1

launch_runs synth_1 -jobs 10
wait_on_run synth_1
launch_runs impl_1 -to_step write_bitstream -jobs 10
wait_on_run impl_1
