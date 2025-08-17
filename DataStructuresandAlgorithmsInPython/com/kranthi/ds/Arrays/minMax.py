def getMinMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]

    print("min: {} and max: {}".format(min, max))


getMinMax([2,4,2,99,8,77,3,1,77])