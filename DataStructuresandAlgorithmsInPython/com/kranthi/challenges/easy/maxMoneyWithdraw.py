"""
Maximum money that can be withdrawn in two steps
Last Updated : 10 May, 2019
There are two cash lockers, one has X number of coins and the other has Y number of coins, you can withdraw money at max two times, when you withdraw from a locker you will get the total money of the locker and the locker will be refilled with Z – 1 coins if it had Z coins initially. The task is to find the maximum coins you can get.

Examples:

Input: X = 6, Y = 3
Output: 11
Take from locker X i.e. 6
Now, X = 5 and Y = 3
Take again from locker X i.e. 5.

Input: X = 4, Y = 4
Output: 8
"""

def maxCoins(x, y):
    if (x < y):
        x, y = y, x