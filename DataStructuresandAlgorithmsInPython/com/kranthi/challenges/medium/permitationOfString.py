"""
Write a program to print all permutations of a given string
Last Updated: 03-12-2020
A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of an
ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.

Source: Mathword(http://mathworld.wolfram.com/Permutation.html)

Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB
"""
def toString(lst:list) -> str:
    return "".join(lst)

def  permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


string = "ABC"
n = len(string)
lst = list(string)
permute(lst, 0, n-1)
