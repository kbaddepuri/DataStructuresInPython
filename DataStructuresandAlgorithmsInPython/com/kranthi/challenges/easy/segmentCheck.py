"""
Check if a key is present in every segment of size k in an array
Last Updated: 15-10-2018
Given an array arr[] and size of array is n and one another key x, and give you a segment size k. The task is to find
that the key x present in every segment of size k in arr[].

Examples:

Input :
arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3}
x = 3
k = 3
Output : Yes
There are 4 non-overlapping segments of size k in the array, {3, 5, 2}, {4, 9, 3}, {1, 7, 3} and {11, 12, 3}. 3 is
present all segments.

Input :
arr[] = { 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25}
x = 23
k = 5
Output :Yes
There are three segments and last segment is not full {21, 23, 56, 65, 34}, {54, 76, 32, 23, 45} and {21, 23, 25}.
23 is present all window.

Input :arr[] = { 5, 8, 7, 12, 14, 3, 9}
x = 8
k = 2
Output : No
"""
def checkSegment(arr:list, key:int, subarryLn:int):
    ls = []
    found = False
    for i in range(len(arr)):
        if len(ls) == subarryLn:
            print(ls, end=" ")
            print(found)
            found = False
            ls = []
        else:
            ls.append(arr[i])
            if not found:
                found = (arr[i] == key)
    if ls:
        print(ls, end=" ")
        print(found)
checkSegment([3, 5 ], 3, 3)