
def slidingWindow(arr, k):
    current_max = 0
    for i in range(k):
        current_max += arr[i]

    max_sum = current_max
    starting = k - 2
    ending = -1
    while starting > -2:
        current_max = current_max - arr[starting+1] + arr[ending]
        if current_max > max_sum:
            max_sum = current_max

        starting -= 1
        ending -= 1

    return max_sum


a=  [1, 3, 3, 1, 4, 5, 2, 8, -1]
print(slidingWindow(a, 3))