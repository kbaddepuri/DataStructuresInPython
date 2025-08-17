def reverseArray(arr, start, end):
    while start < end:
        if arr[start] != arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def reverseArrayInRecursive(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverseArrayInRecursive(arr, start + 1, end - 1)


print(reverseArrayInRecursive([1, 2, 3, 4, 5], 0, 4))
