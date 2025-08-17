"""
Print words of a string in reverse order
Last Updated: 27-12-2018
Let there be a string say “I AM A GEEK”. So, the output should be “GEEK A AM I”.
This can done in many ways. One of the solutions is given in Reverse words in a string .

Examples:

Input : I AM A GEEK
Output : GEEK A AM I

Input : GfG IS THE BEST
Output : BEST THE IS GfG
"""

def reverseLine(string):
    n = len(string)
    start = n - 1
    end = n
    result = ""
    tmp = ""
    for i in range(n-1, -1, -1):
        if string[i] == ' ':
            result += string[start + 1: end]
            result+= string[i]
            end = i
            start = end - 1
        else:
            start -= 1

    if start !=end:
        result += string[start+1:end]
    print(result)


reverseLine("I AM A GEEK")



