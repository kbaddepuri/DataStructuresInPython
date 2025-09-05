
'''
Second Largest Element in an Array

Time Complexity: O(n)
Space Complexity: O(1)
'''

def secondLargest(arr: list, size: int) -> int:
    if size < 2:
        return None
    
    first = second = float('-inf')
    
    for i in range(size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
            
    return second

arr = [12, 35, 1, 10, 34, 1]
size = len(arr)
print("Second largest element is:", secondLargest(arr, size))