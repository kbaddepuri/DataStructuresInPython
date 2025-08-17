"""
Increase  given array by one

for example:
input -> [1,2,5,6]
output -> [1,2,5,7]
"""


def increaseValuue(arr):
    if len(arr) == 0:
        return arr

    result = [0] * (len(arr))
    carry = 1
    for i in range(len(arr) - 1, -1, -1):
        total = arr[i] + carry
        if total == 10:
            carry = 1
        else:
            carry = 0

        result[i] = total % 10

    if carry == 1:
        result.insert(0, carry)
    return result



arr = [9,9,9,9,9]
print(increaseValuue(arr))

