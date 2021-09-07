`timescale 1ns / 1ps

module RRAM_CTRL #(parameter g_RRAM_INV=0, g_RRAM_CELLS=64)(
    input  clk,
    input  rst,
    input  tx_dv,
    output reg tx_en,
    output reg [63:0] tx_reg
);
    
    reg  [g_RRAM_CELLS-1:0] en;
    wire [g_RRAM_CELLS-1:0] inv_2;

    reg tx_reg_out = 1'b0, tx_reg_header = 1'b0;
    reg en_reg_low = 1'b0, en_reg_high = 1'b0;

    reg wait_count_en=1'b0, en_count_en=1'b0;
    reg [1:0] wait_count = 2'h0;
    reg [6:0] en_count = 7'h00;
    
    reg [3:0] state, nextState;
    localparam S_start=4'h0, S_low_en=4'h1, S_low_wait=4'h2, S_low_write=4'h3, S_low_serial_en=4'h4, S_low_serial_wait=4'h5, S_high_en=4'h6, S_high_wait=4'h7, S_high_write=4'h8, S_high_serial_en=4'h9, S_high_serial_wait=4'hA;

    
    //RRAM Cells
    RRAM #(
        .g_RRAM_INV(g_RRAM_INV),
        .g_RRAM_CELLS(g_RRAM_CELLS)
    ) rram (
        .en(en),
        .inv_2(inv_2)
    );

    //FSM - Next State Transition
    always @(posedge clk)
    begin : FSM_SEQ
        if (rst)
            state <= S_start;
        else
            state <= nextState;
    end
    
    //FSM - Output Logic
    always @ (posedge clk)
    begin : OUTPUT_LOGIC
        if (rst) begin
            en_reg_low    <= 1'b0;
            en_reg_high   <= 1'b0;
            en_count_en   <= 1'b0;
            wait_count_en <= 1'b0;
            tx_en         <= 1'b0;
            tx_reg_header <= 1'b0;
            tx_reg_out    <= 1'b0;
        end
        else begin
            case(state)
                S_start: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b1;
                    tx_reg_out    <= 1'b0;
                end
                S_low_en: begin
                    en_reg_low    <= 1'b1;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b1;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                S_low_wait: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b1;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                S_low_write: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b1;
                end
                S_low_serial_en: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b1;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                S_low_serial_wait: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                S_high_en: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b1;
                    en_count_en   <= 1'b1;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                S_high_wait: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b1;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                S_high_write: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b1;
                end
                S_high_serial_en: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b1;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                S_high_serial_wait: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
                default: begin
                    en_reg_low    <= 1'b0;
                    en_reg_high   <= 1'b0;
                    en_count_en   <= 1'b0;
                    wait_count_en <= 1'b0;
                    tx_en         <= 1'b0;
                    tx_reg_header <= 1'b0;
                    tx_reg_out    <= 1'b0;
                end
            endcase
        end
    end
    
    //FSM - Next State Logic    
    always @ (state, wait_count, tx_dv, en_count)
    begin : FSM_COMBO
        nextState = 4'h0;
        case(state)
            S_start:
                nextState = S_high_serial_en;
            S_low_en:
            begin
                if(en_count < 7'hFF) nextState = S_low_wait;
                else                 nextState = S_low_write;
            end
            S_low_wait:
            begin
                if(wait_count < 2'hF) nextState = S_low_wait;
                else                  nextState = S_low_en;
            end
            S_low_write:
                nextState = S_low_serial_en;
            S_low_serial_en:
                nextState = S_low_serial_wait;
            S_low_serial_wait:
            begin
                if(tx_dv) nextState = S_low_serial_wait;
                else      nextState = S_high_wait;
            end
            S_high_en:
            begin
                if(en_count < 7'hFF) nextState = S_high_wait;
                else                 nextState = S_high_write;
            end
            S_high_wait:
            begin
                if(wait_count < 2'hF) nextState = S_high_wait;
                else                  nextState = S_high_en;
            end
            S_high_write:
                nextState = S_high_serial_en;
            S_high_serial_en:
                nextState = S_high_serial_wait;
            S_high_serial_wait:
            begin
                if(tx_dv) nextState = S_high_serial_wait;
                else      nextState = S_low_wait;
            end
            default:
                nextState = S_start;
        endcase
    end

    //Update en_reg
    always @(posedge clk)
    begin
        if (rst)
            en <= 64'h0000000000000000;
        else if(en_reg_low)
            en <= {en[g_RRAM_CELLS-2:0],1'b0};
        else if(en_reg_high)
            en <= {en[g_RRAM_CELLS-2:0],1'b1};
    end

    //Update tx_reg
    always @(posedge clk)
    begin
        if (rst)
            tx_reg <= 64'h0000000000000000;
        else if(tx_reg_header)
            //ASCII =     CRNLR-R-A-M-CRNL;
            tx_reg <= 64'h0D0A5252414D0D0A;
        else if (tx_reg_out)
            tx_reg <= {{64-g_RRAM_CELLS{1'b1}},inv_2[g_RRAM_CELLS-1:0]};
    end

    //Wait Count
    always @(posedge clk)
    begin
        if (rst)
            wait_count <= 2'h0;
        else if (wait_count_en)
            wait_count <= wait_count + 1;
    end

    //Wait Count
    always @(posedge clk)
    begin
        if (rst)
            en_count <= 6'h00;
        else if (en_count_en)
            en_count <= en_count + 1;
    end
endmodule

