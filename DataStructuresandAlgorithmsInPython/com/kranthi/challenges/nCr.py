"""
A bianomial coefficient can also gives the number of ways disregarding order, that k objects can be chosen from among
n objects; more formally, the number of k-element subsets (or k-combinations) of an n-element set


nCr = n!/ r!(n-r)!

"""


def nCr(n: int, r: int) -> int:
    return int(fact(n) / (fact(r) * fact(n - r)))


def fact(n: int) -> int:
    res = 1

    for i in range(2, n + 1):
        res = res * i

    return res


print(nCr(50, 40))
