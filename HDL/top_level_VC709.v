`timescale 1ns / 1ps

module top_level(
    input  clk_p,
    input  clk_n,
    input [4:0] BUTTON,
    output TX
    );
    
    wire rst;
    wire clkin1, clk_100, clk_10;
    wire [63:0] tx_reg;
    wire tx_en, tx_dv;
    wire [7:0] temp;

    //Input Clk buffer
    IBUFGDS clkin1_buf(
        .O  (clkin1),
        .I  (clk_p),
        .IB (clk_n)
    );

    //Clk Divider - MMCM
    CLK_DIV #(
        .MULTI(3.0)
    ) clk_div(
        .clkin1(clkin1),
        .rst(rst),
        .clk_out_10(clk_10)
    );

    //Button Debouncer
    DEBOUNCER #(
        .DELAY(8)
    ) db (
        .clk(clkin1),
        .IN(BUTTON[0]),
        .OUT(rst)
    );

    //Output Serial Data
    UART_CTRL uart_ctrl(
        .clk(clk_10),
        .rst(rst),
        .tx_reg(tx_reg),
        .tx_en(tx_en),
        .tx_busy(tx_dv),
        .tx(TX)
    );
    
    //RRAM controler
    RRAM_CTRL #(
        .g_RRAM_INV(5),//1,3,5,7
        .g_RRAM_CELLS(64)
    ) rram_ctrl (
        .clk(clk_10),
        .rst(rst),
        .tx_dv(tx_dv),
        .tx_en(tx_en),
        .tx_reg(tx_reg)
    );


endmodule
