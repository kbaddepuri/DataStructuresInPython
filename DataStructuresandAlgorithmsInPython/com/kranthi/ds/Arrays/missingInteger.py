"""
with summutation formula, we can calculate sum of n-1 values with n*(n+1)/2 formula. for n elememtns
(n+1)*(n+2)/2
"""


def missingIntger(arr):
    n = len(arr)
    total = (n+1)*(n+2)//2
    sum_ = sum(arr)

    return total - sum_

a = [1,2,4,5,6,7,8]
print(missingIntger(a))