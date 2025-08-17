"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which,
together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.
"""
from typing import List


def maxVolume(heights:List[int]) ->int:
    # 1. Define maxVolume, left and right and this is two pointer approach
    maxVolume = 0
    # 2. left points to starting element and right points to end of the element in list
    left = 0
    right = len(heights) - 1
    while right > left:
        # 3. volume for current values: volume = minimum in two values * difference of width in two pointers
        currentMax = min(heights[left], heights[right]) * (right - left)
        # 4. Store max volume in maxVolume
        maxVolume = max(maxVolume, currentMax)
        # 5. increase left point to by 1 if left value is less than right otherwise decrease right pointer by 1
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return maxVolume