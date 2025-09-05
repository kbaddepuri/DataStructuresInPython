"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""
def multiplyStrings(num1:str, num2:str) -> str:
    n1, n2 = 0, 0
    mul = 1
    for i in range(len(num1) - 1, -1, -1):
        n1 = mul * int(num1[i]) + n1
        mul = mul * 10

    mul = 1
    for i in range(len(num2) - 1, -1, -1):
        n1 = mul * int(num2[i]) + n1
        mul = mul * 10

    res = n1 * n2
    return str(res)