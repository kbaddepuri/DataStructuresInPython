"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        start, end = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return  left + 1, right - 1

        for i in range(len(s)):
            # for odd length
            l1, r1 = expand(i , i)

            # for even
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start: end + 1]

s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("abab"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("abab"))
print(s.longestPalindrome("ababbbbb"))
print(s.longestPalindrome("ababab"))
