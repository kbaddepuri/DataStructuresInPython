"""
input: 4562
output: 2654
"""

def reverseDigits(num):
    rev = 0
    while num > 0:
        a = num % 10
        rev = rev * 10 + a
        num = num // 10

    print(rev)


reverseDigits(4562)
