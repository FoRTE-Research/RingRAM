`timescale 1ns / 1ps

module DEBOUNCER#(parameter DELAY=8)(
    input clk,
    input IN,
    output OUT
);
    reg [DELAY-1:0] shift_reg={DELAY{1'b0}};

    //Wait for stable
    assign OUT = (shift_reg=={DELAY{1'b1}}) ? 1'b1 : 1'b0;

    //Input Shift Register
    always @ (posedge clk) 
    begin
        shift_reg <= {shift_reg[DELAY-2:0],IN};
    end
endmodule
