class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {n - 1:0}
        dp = [float("inf")] * (n)
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            val = float("inf")
            for j in range(1, nums[i] + 1):
                if i + j <= n - 1:
                    dp[i] = min(dp[i + j] + 1, dp[i])
                    # print(dp[i])
                else:
                    break

        return dp[0]