# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start Mealy machine test")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # Test sequence: 1010
    dut._log.info("Testing sequence 1010")
    
    # Input: 1
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0, "Output should be 0 after first 1"
    
    # Input: 0
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0, "Output should be 0 after 10"
    
    # Input: 1
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0, "Output should be 0 after 101"
    
    # Input: 0 - Complete sequence 1010
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1, "Output should be 1 after detecting 1010"
    
    dut._log.info("Sequence 1010 detected successfully!")
    
    # Test another sequence: 11010
    dut._log.info("Testing sequence 11010")
    
    # Input: 1
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0
    
    # Input: 1
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0
    
    # Input: 0
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0
    
    # Input: 1
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0
    
    # Input: 0 - Complete sequence 11010
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1, "Output should be 1 after detecting 11010"
    
    dut._log.info("All tests passed!")
