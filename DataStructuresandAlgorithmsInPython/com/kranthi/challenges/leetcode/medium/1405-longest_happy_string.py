"""
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".



Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
"""
# this can be done using greedy algorithm

def longestHappyString(a, b, c):
    available = {'a':a, 'b':b, 'c':c}
    ans = ['x', 'x'] # dummy chars to ensure while loop continues
    while sum(available.values()) > 0:
        pic_max_available = ''

        for ch in available.keys():
            if available[ch] > 0 and not (ans[-1] == ch and ans[-2] == ch):
                if not pic_max_available:
                    pic_max_available = ch

                elif available[ch] > available[pic_max_available]:
                    pic_max_available = ch

        if not pic_max_available:
            break
        ans.append(pic_max_available)
        available[pic_max_available] -= 1

    return ''.join(ans[2:])


print(longestHappyString(2, 2, 1))