"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending
order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List

"""
Solution: use greedy algorithm
1. start from n-2
2. Compare current element with next element
    a. if current element is less than next element then break
3. if values read in array reached to starting of the array, which means, all valueas are sorted in descending order
    so next increment permutation is not possible, sort the array and return
4. If found, then loop from last element to till the value found in step 2
5. If current value is greater than element found in 2, then swap current with element found in step 2
6. sort the array remaining array after element found in step 2 to till last 

time complexity: O(n), space compexity: O(1)
"""


def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    if n < 2:
        return nums
    start = n - 2
    while start >= 0:
        if nums[start] < nums[start + 1]:
            break
        else:
            start -= 1
    if start == -1:
        nums.sort()
        return
    for i in range(n - 1, start, -1):
        if nums[i] > nums[start]:
            nums[start], nums[i] = nums[i], nums[start]
            nums[start + 1:] = sorted(nums[start + 1:])
            break
    return
