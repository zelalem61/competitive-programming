class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for s in range(n):
            for i in range(n-s):
                j = i + s
                if i == j:
                    dp[i][i] = nums[i]
                else:
                    pick_left = nums[i] - dp[i+1][j]
                    pick_right = nums[j] - dp[i][j-1]
                    dp[i][j] = max(pick_left, pick_right)
        return dp[0][-1] >= 0
        