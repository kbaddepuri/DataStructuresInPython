"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
 and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""
from typing import List

"""
Solution: 
1. Since we need three distinct values, we need to sort array first.
2. Fix last value and find the remaining two values which will give sum to 0
    a. fix last
    b. iterate from 0 to last - 1 so that overal sum is 0
3. repeat the same for all the elements and save the distinct three values in set
"""


def threeSum(array: List[int]) -> List[List[int]]:
    added = set()
    array.sort()
    for i in range(len(array) - 1, -1, -1):
        last = array[i]
        start = 0
        end = i - 1
        while start < end:
            s = array[start] + array[end] + last
            if s == 0:
                added.add([array[start], array[end], last])
                start += 1
            elif s > 0:
                end -= 1
            else:
                start += 1
    return list(added)
