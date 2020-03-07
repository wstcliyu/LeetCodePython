class Uncrossed_1035:
    # 2D DP
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


    # 1D DP
    # The inner loops must be separated
    # The first inner loop must be in reverse order
    # def maxUncrossedLines(self, A, B):
    #     m, n = len(A), len(B)
    #     dp = [0] * (n + 1)
    #     for i in range(m):
    #         for j in range(n)[::-1]:
    #             if A[i] == B[j]: dp[j + 1] = dp[j] + 1
    #         for j in range(n):
    #             dp[j + 1] = max(dp[j + 1], dp[j])
    #     return dp[n]


    # 2D DP
    # def maxUncrossedLines(self, A, B):
    #     dp, m, n = collections.defaultdict(int), len(A), len(B)
    #     for i in xrange(m):
    #         for j in xrange(n):
    #             dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
    #     return dp[m - 1, n - 1]