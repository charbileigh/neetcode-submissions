class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        lengths = 0
        n = len(s)

        for i in range(n):
            for left, right in [(i, i), (i, i + 1)]:
                while left >= 0 and right < n and s[left] == s[right]:
                    length = right - left + 1
                    if length > lengths:
                        start = left
                        lengths = length

                    left -= 1
                    right += 1
        return s[start:start + lengths]