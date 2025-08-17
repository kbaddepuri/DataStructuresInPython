"""
Minimum Increment / decrement to make array elements equal

Given an array of integers where ￼. In one operation you can either Increment/Decrement any element by 1. The task is to find the minimum operations needed to be performed on the array elements to make all array elements equal.
Examples:


Input : A[] = { 1, 5, 7, 10 }
Output : 11
Increment 1 by 4, 5 by 0.
Decrement 7 by 2, 10 by 5.
New array A = { 5, 5, 5, 5 } with
cost of operations = 4 + 0 + 2 + 5 = 11.

Input : A = { 10, 2, 20 }
Output : 18
"""

def solution(A:list):
    n = len(A)
    A.sort()

    step_needed = 0
    mid = A[int(n/2)]

    for i in range(0, n):
        step_needed = step_needed + abs(A[i] - mid)

    # If array has even length, then we need to re-calculate the steps
    # by calculatng the both middle elements
    if n%2 == 0:
        temp_step_needed = 0
        mid = A[int(n/2) - 1]

        for i in range(0, n):
            temp_step_needed = temp_step_needed + abs(A[i] - mid)

        step_needed = min(step_needed, temp_step_needed)


    return step_needed

print(solution([3,2,1,1,2,3,1]))
