"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
"""

def reverse(x:int) -> int:
    val = 0
    mul = 10
    isNegative = False
    if x < 0:
        isNegative = True
        x = -x
    while x > 0:
        val = val*mul + x%10
        x = x//10
    _range = pow(2, 31)
    if (-_range <= val <= _range - 1):
        if isNegative:
            val  = -val
        return val
    return 0