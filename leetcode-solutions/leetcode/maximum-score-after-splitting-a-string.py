class Solution:
    def maxScore(self, s: str) -> int:
        nums = []
        ans = 0
        for st in s:
            nums.append(int(st))
        for i in range(1,len(nums)):
            res1 = sum(nums[:i])
            res2 = sum(nums[i:len(nums)])
            res = i-res1 + res2
            ans = max(ans,res)
        return ans
