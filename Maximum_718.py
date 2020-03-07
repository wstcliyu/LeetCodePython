class Maximum_718:
	# Time: O(max(M, N) lg min(M, N))
	# Space: O(max(M, N))
	def findLength(self, A: List[int], B: List[int]) -> int:
        def check(length):
            seen = {A[i:i+length] for i in range(len(A) - length + 1)}
            return any(B[j:j+length] in seen for j in range(len(B) - length + 1))
        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        lo, hi = 0, 1 + min(len(A), len(B))
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1


    # Time: O(MN)
    # Space: O(MN), can be improved to 1D DP
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
        return max(max(row) for row in dp)