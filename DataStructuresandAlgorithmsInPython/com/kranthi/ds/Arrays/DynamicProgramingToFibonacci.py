
def fib_botton_up(n):
    if n == 0 or n == 1:
        return 1
    # bottom_up = [0, 1]
    # bottom_up.extend([0]*(n-1))
    bottom_up = [0] * n
    bottom_up[0] = 0
    bottom_up[1] = 1

    for i in range(2, n):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

    return bottom_up

print(fib_botton_up(9))

