`timescale 1ns / 1ps

module UART_CTRL#(parameter g_CLKS_PER_BIT=87)(
    input  clk,
    input  rst,
    input  [63:0] tx_reg,
    input  tx_en,
    output tx_busy,
    output tx
);
    wire tx_dv, tx_done, tx_active;
    wire [7:0] data_tx;
    reg  [3:0] tx_count= 4'h0;

    UART_TX #(
        .g_CLKS_PER_BIT(87)
        //100MHz/115200=868
        //10MHz/115200=87
    ) uart_tx (
        .i_Clk(clk),
        .i_TX_DV(tx_dv),
        .i_TX_Byte(data_tx),
        .o_TX_Active(tx_active),
        .o_TX_Serial(tx),
        .o_TX_Done(tx_done)
    );

    //SERIAL_COUNT
    always @(posedge clk)
    begin
        if (rst)
            tx_count <= 4'h0;
        else if (tx_en)
            tx_count <= 4'h0;
        else if (tx_done==1'b1 & tx_active==1'b0)
            tx_count <= tx_count + 1;
    end

    assign data_tx = tx_count == 4'h0 ? tx_reg[63:56] :
                     tx_count == 4'h1 ? tx_reg[55:48] :
                     tx_count == 4'h2 ? tx_reg[47:40] :
                     tx_count == 4'h3 ? tx_reg[39:32] :
                     tx_count == 4'h4 ? tx_reg[31:24] :
                     tx_count == 4'h5 ? tx_reg[23:16] :
                     tx_count == 4'h6 ? tx_reg[15:8]  :
                     tx_count == 4'h7 ? tx_reg[7:0]   :
                     4'h0;

    assign tx_dv = tx_count < 4'h8 ? 1 : 0;

    assign tx_busy = tx_dv | tx_active; 
endmodule
