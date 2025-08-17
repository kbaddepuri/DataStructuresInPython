"""
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example,
if  left rotations are performed on array , then the array would become .

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a
single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of  (the number of integers) and
(the number of left rotations you must perform).
The second line contains  space-separated integers describing the respective elements of the array's initial state.

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:

Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4.
"""


def left_rotation(arr, dist):
    while dist > 0:
        v = arr.pop(0)  # delete value from the beginning and get that value as pop() method returns the deleted value
        arr.append(v)  # Append function will always append value at the end of list
        dist -= 1
    for i in arr:
        print(i, end=" ")


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    left_rotation(a, d)
