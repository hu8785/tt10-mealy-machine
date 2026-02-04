<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This is a Mealy machine implementation with 5 states (a, b, c, d, e) that detects the sequence 1010.

- State a: Initial state
- State b: After detecting first '1'
- State c: After detecting '10'
- State d: After detecting '101'
- State e: After detecting '1010' (output = 1)

The output depends on both the current state and input, which is the characteristic of a Mealy machine. When the complete sequence 1010 is detected, the output goes high.

## How to test

1. Reset the design by asserting the reset signal
2. Apply input sequence on ui[0]
3. Observe output on uo[0]
4. The output should go high when the sequence 1010 is detected
5. Test with different input sequences to verify correct operation

## External hardware

No external hardware required. Just connect input and observe output.
