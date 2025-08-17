
"""
Fibonacci using O(n)
Note that if we use recurssion then it would become exponential ie O(n!)
"""

def fibonacciSumOfNo(n: str) -> str:
    num1 = 0
    num2 = 1

    if n == 1:
        return num1

    if n == 2:
        return num2

    count = 1
    c = 0
    sumN = 0
    while count < n:
        c = num1 + num2
        num1 = num2
        num2 = c
        count += 1
        sumN = sumN + num1

    return sumN

print(fibonacciSumOfNo(9))
