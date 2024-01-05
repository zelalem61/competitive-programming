class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        left = 1
        right = len(nums)-1
        res = set()
        nums.sort()
        while i < len(nums):
            while left < right:
                if i > 0 and nums[i] == nums[i-1]:
                    break
                if nums[i]+nums[left]+nums[right] == 0:
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left += 1
                else:
                    right -= 1
                    # -4,-1,-1,0,1,2
            i+=1
            left = i+1
            right = len(nums)-1
        return res
        