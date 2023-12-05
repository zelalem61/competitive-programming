class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        permeter = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                permeter = max(permeter, nums[i] + nums[i+1] + nums[i+2])
        return permeter
