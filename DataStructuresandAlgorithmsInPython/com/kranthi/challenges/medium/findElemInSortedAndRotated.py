"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""


# Search an element in sorted and rotated array using
# single pass of Binary Search

def simpleBinarySearch(arr, l, r, key):
    if l > r:
        return -1
    mid = (l + r) // 2
    if arr[mid] == key:
        return mid

    if arr[mid] < key:
        return search(arr, mid + 1, r, key)
    return search(arr, l, mid - 1, key)


def search(arr, l, r, key):
    if l > r:
        return -1
    mid = (l + r) // 2
    if arr[mid] == key:
        return mid

    # if arr[l,,mid] is sorted
    if arr[l] <= arr[mid]:
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if arr[l] <= key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, r, key)

    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if arr[mid] <= key <= arr[r]:
        return search(arr, mid + 1, r, key)
    return search(arr, l, mid - 1, key)


# Driver program
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 1
i = search(arr, 0, len(arr) - 1, key)
if i != -1:
    print("Index: % d" % i)
else:
    print("Key not found")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Index: {simpleBinarySearch(arr, 0, len(arr) - 1, 6)}")
