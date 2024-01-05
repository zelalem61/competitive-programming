class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        i = 0
        left = 1
        right = len(nums) - 1

        while i < len(nums):
            while left < right:
                print(nums[left])
                summ = nums[i]+nums[left]+nums[right]
                if abs(summ-target) < abs(res-target):
                    res = summ
                if summ - target == 0:
                    return summ
                elif summ - target > 0:
                    right-=1
                else:
                    left+=1
            i += 1
            left = i+1
            right = len(nums) - 1
        return res

