class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxSum = nums[0]
        for right in range(len(nums)):
            if summ + nums[right] < 0:
                maxSum = max(maxSum,nums[right])
                summ = 0
            else:
                summ+=nums[right]
                maxSum = max(summ,maxSum)
        return maxSum
