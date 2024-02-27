class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(s=[], nums=[]):
            if len(s) == len(nums):
                result.append(s)
                return
            for i in range(len(nums)):
                if nums[i] not in s:
                    solve(s + [nums[i]], nums)
        solve([], nums)
        return result