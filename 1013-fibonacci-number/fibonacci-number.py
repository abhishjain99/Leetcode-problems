class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        # # Recursion
        # return self.fib(n-1) + self.fib(n-2)

        # DP
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]