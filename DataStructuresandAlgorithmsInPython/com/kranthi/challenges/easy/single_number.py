"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""


"""
solution:
=========
Concept

If we take XOR of zero and some bit, it will return that bit
a⊕0=a
If we take XOR of two same bits, it will return 0
0a⊕a=0
ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
So we can XOR all bits together to find the unique number.


"""

def single_number(nums: list) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a

print(single_number([1,2,3,1,2,4,3]))