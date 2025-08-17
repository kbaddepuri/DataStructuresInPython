def diff(arr, n):
    max_dff = arr[1] - arr[0]
    min_elem = arr[0]

    for i in range(1, n):
        if arr[i] - min_elem > max_dff:
            max_dff = arr[i] - min_elem

        if min_elem > arr[i]:
            min_elem = arr[i]

    return max_dff


print(diff([10,2,3,4,5,6,10], 7))
