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
Explanation: It's the only correct answer in this case
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    all_chars = {'a': A, 'b': B, 'c': C}
    diverse_str = ['d', 'd']  # Just dummy characters to ensure while loop continues

    # While there are still characters left to add
    while sum(all_chars.values()) > 0:
        pick_max_available = ''

        for ch in all_chars.keys():

            # If character addition is valid
            if all_chars[ch] > 0 and not (diverse_str[-1] == ch and diverse_str[-2] == ch):

                # Assign if not picked yet
                if not pick_max_available:
                    pick_max_available = ch

                # Reassign character with larger count -- Greedy
                elif all_chars[ch] > all_chars[pick_max_available]:
                    pick_max_available = ch

        # If no more possible options ==> exit
        if not pick_max_available:
            break

        diverse_str.append(pick_max_available)
        all_chars[pick_max_available] -= 1
    print(''.join(diverse_str[2:]))
    return ''.join(diverse_str[2:])  # Exclude first two dummy characters

solution(6,7,10)
