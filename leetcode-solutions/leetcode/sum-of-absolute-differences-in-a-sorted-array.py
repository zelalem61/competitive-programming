class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums))
        n = len(nums)
        res = []
        for i in range(n):
            difSum = ((i+1)*(nums[i]) - prefix[i]) + ((prefix[-1] - prefix[i]) - (n-i-1)*nums[i])
            res.append(difSum)
        return res
         