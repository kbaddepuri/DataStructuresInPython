"""
Compute nCr % p | Set 1 (Introduction and Dynamic Programming Solution)
A Simple Solution is to first compute nCr, then compute nCr % p. This solution works fine when the value of nCr is
small.

What if the value of nCr is large?
The value of nCr%p is generally needed for large values of n when nCr cannot fit in a variable, and causes overflow.
So computing nCr and then using modular operator is not a good idea as there will be overflow even for slightly larger
values of n and r. For example the methods discussed here and here cause overflow for n = 50 and r = 40.

The idea is to compute nCr using below formula






   C(n, r) = C(n-1, r-1) + C(n-1, r)
   C(n, 0) = C(n, n) = 1
Working of Above formula and Pascal Triangle:
Let us see how above formula works for C(4, 3)

1==========>> n = 0, C(0, 0) = 1
1–1========>> n = 1, C(1, 0) = 1, C(1, 1) = 1
1–2–1======>> n = 2, C(2, 0) = 1, C(2, 1) = 2, C(2, 2) = 1
1–3–3–1====>> n = 3, C(3, 0) = 1, C(3, 1) = 3, C(3, 2) = 3, C(3, 3)=1
1–4–6–4–1==>> n = 4, C(4, 0) = 1, C(4, 1) = 4, C(4, 2) = 6, C(4, 3)=4, C(4, 4)=1
So here every loop on i, builds i’th row of pascal triangle, using (i-1)th row

Extension of above formula for modular arithmetic:
We can use distributive property of modulor operator to find nCr % p using above formula.

   C(n, r)%p = [ C(n-1, r-1)%p + C(n-1, r)%p ] % p
   C(n, 0) = C(n, n) = 1
"""


def nCrModP(n, r, p):
    if r > n - r:
        r = n - r

    C = [0 for i in range(r + 1)]
    C[0] = 1

    for i in range(1, n + 1):
        # Fill entries of current row
        # using previous row values
        for j in range(min(i, r), 0, -1):
            # nCj = (n-1)C(j-1) + (n-1)Cj
            C[j] = (C[j] + C[j-1]) % p
    return C[r]

print(__file__)