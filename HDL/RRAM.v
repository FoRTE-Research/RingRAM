`timescale 1ns / 1ps

module RRAM #(parameter g_RRAM_INV=5, g_RRAM_CELLS=64)(
    input  [g_RRAM_CELLS-1:0] en,
    output [g_RRAM_CELLS-1:0] inv_2
);
    
    wire [g_RRAM_CELLS-1:0] and_1, and_2, inv_1;
    wire [g_RRAM_CELLS-1:0] en_buff;
    wire [g_RRAM_INV-1:0] inv_buff_1[g_RRAM_CELLS-1:0];
    wire [g_RRAM_INV-1:0] inv_buff_2[g_RRAM_CELLS-1:0];

    genvar i,j;
    generate
        for (i=0; i<g_RRAM_CELLS; i=i+1)
        begin
            (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)BUF g_en_buff(
                .I(en[i]),
                .O(en_buff[i])
            );

            (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)BUF g_out_buff_1(
                .I(inv_buff_1[i][g_RRAM_INV-1]),
                .O(inv_1[i])
            );
                
            (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)BUF g_out_buff_2(
                .I(inv_buff_2[i][g_RRAM_INV-1]),
                .O(inv_2[i])
            );
            
            (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)my_and g_and_1(
                .a(en_buff[i]),
                .b(inv_buff_2[i][g_RRAM_INV-1]),
                .o(and_1[i])
            );
            
            (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)my_and g_and_2(
                .a(en_buff[i]),
                .b(inv_buff_1[i][g_RRAM_INV-1]),
                .o(and_2[i])
            );
            
            for (j=0; j<g_RRAM_INV; j=j+1)
            begin
                if (j==0) begin
                    (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)my_not g_inv_buff_1( 
                        .a(and_1[i]),
                        .o(inv_buff_1[i][j])
                    );
                    
                    (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)my_not g_inv_buff_2( 
                        .a(and_2[i]),
                        .o(inv_buff_2[i][j])
                    );
                end
                else begin
                    (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)my_not g_inv_buff_1( 
                        .a(inv_buff_1[i][j-1]),
                        .o(inv_buff_1[i][j])
                    );
                    
                    (* ALLOW_COMBINATORIAL_LOOPS = "true", KEEP = "true", DONT_TOUCH="true" *)my_not g_inv_buff_2( 
                        .a(inv_buff_2[i][j-1]),
                        .o(inv_buff_2[i][j])
                    );           
                end
            end
        end
    endgenerate
endmodule
