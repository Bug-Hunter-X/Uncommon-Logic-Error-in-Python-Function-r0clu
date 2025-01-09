# Uncommon Logic Error in Python

This repository demonstrates a subtle logic error in a Python function that can lead to unexpected results. The function is designed to return either a or b, depending on their values. However, when a division is performed with 0 as the denominator, this leads to a ZeroDivisionError, which would cause the function to terminate early. The error is not immediately obvious due to the simple structure of the function.

## Bug Description

The `function_with_uncommon_error` function includes an `else` block which attempts a division. If `b` is 0, a `ZeroDivisionError` occurs.  This error isn't immediately obvious to those who might not anticipate the use of division in the `else` block. 

## Solution

The solution addresses this issue by adding an explicit check for division by zero before performing the operation.