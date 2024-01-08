class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cur = 0 
        l = 0 
        res = 0
        for r, num in enumerate(nums):
            if num == 0:
                if cur < k:
                    cur += 1
                else:
                    while nums[l] == 1 and l < r:
                        l += 1
                    l += 1
            res = max(res, r - l + 1)
        return res
        