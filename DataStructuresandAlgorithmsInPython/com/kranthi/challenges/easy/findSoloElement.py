# function to find the once
# appearing element in array
def findSingle(arr):
    data = {}

    for i in arr:
        if i not in data:
            data[i] = 1
        else:
            data[i] = data[i] + 1

    if data.keys():
        vals = [key for key, val in data.items() if val == 1]
        if vals:
            return vals[0]
    return 0


# Driver code
ar = [2, 2, 3, 5, 7, 5, 4, 8, 7, 8, 4, 5, 3, 11,4]
print("Element occurring once is", findSingle(ar))

