`timescale 1ns / 1ps

module my_nand(
    input  a,
    input  b,
    output o
);
    assign o = !( a & b );
endmodule
