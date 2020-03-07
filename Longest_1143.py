class Longest_1143:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(n)[::-1]:
                if text1[i] == text2[j]:
                    dp[j + 1] = 1 + dp[j]
            for j in range(n):
                dp[j + 1] = max(dp[j], dp[j + 1])
        return dp[-1]