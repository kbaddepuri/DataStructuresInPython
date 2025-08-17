"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

def arrayRotate(arr:list, k:int):
    n = len(arr)
    res = [0]*n
    if k > n:
        k = k-n
    for i in range(n):
        res[(i+k)%n] = arr[i]

    arr[:] = res

arr = [1,2,3,4,5,6,7]
arrayRotate(arr, 11)
print(arr)

