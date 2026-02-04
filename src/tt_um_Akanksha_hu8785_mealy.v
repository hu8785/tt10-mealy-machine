`default_nettype none

module tt_um_Akanksha_hu8785_mealy (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // State encoding
  parameter [2:0] a = 3'b000,  // Initial state
                  b = 3'b001,  // After detecting '1'
                  c = 3'b010,  // After detecting '10'
                  d = 3'b011,  // After detecting '101'
                  e = 3'b100;  // After detecting '1010'

  reg [2:0] state, next_state;
  wire in;
  reg out;

  assign in = ui_in[0];  // Input signal

  // State register
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      state <= a;
    else
      state <= next_state;
  end

  // Next state logic and output logic (Mealy machine)
  always @(*) begin
    out = 1'b0;  // Default output
    case (state)
      a: begin
        if (in) begin
          next_state = b;
          out = 1'b0;
        end else begin
          next_state = a;
          out = 1'b0;
        end
      end
      
      b: begin
        if (in) begin
          next_state = b;
          out = 1'b0;
        end else begin
          next_state = c;
          out = 1'b0;
        end
      end
      
      c: begin
        if (in) begin
          next_state = d;
          out = 1'b0;
        end else begin
          next_state = a;
          out = 1'b0;
        end
      end
      
      d: begin
        if (in) begin
          next_state = b;
          out = 1'b0;
        end else begin
          next_state = e;
          out = 1'b1;  // Sequence 1010 detected!
        end
      end
      
      e: begin
        if (in) begin
          next_state = b;
          out = 1'b0;
        end else begin
          next_state = a;
          out = 1'b0;
        end
      end
      
      default: begin
        next_state = a;
        out = 1'b0;
      end
    endcase
  end

  // Output assignment
  assign uo_out = {7'b0, out};
  assign uio_out = 8'b0;
  assign uio_oe = 8'b0;

endmodule
