def moveAllZerosToRight(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr

print(moveAllZerosToRight([1,0,0,2,3,0,6,7]))