class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                n -= 1
                del nums[i]
            else:
                i += 1
        print(nums)
                    
        return n
        