class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)

        if n == 0:
            return 0
        
        dp = [[0] * n for i in range(n)]

        for l in range(n - 1, -1, -1):
            dp[l][l] = 1

            for r in range(l + 1, n):
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l + 1][r - 1]
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        
        return dp[0][n - 1]