"""
Given two binary strings, return their sum (also a binary string).

Example:

Input:  a = "11", b = "1"
Output: "100"
"""


def add_two_binary_nums(num1:str, num2: str) -> str:
    max_len = max(len(num1), len(num2))

    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len-1, -1, -1):
        temp = carry
        temp += 1 if num1[i] == '1' else 0
        temp += 1 if num2[i] == '1' else 0

        result = ('1' if temp %2 == 1 else '0') + result
        carry = 0 if temp < 2 else 1

    if carry != 0:
        result = '1' + result

    return result



print(add_two_binary_nums('11010', '1011'))