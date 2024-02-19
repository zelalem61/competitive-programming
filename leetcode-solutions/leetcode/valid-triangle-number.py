class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i+1,len(nums) - 1):
                validVal = nums[i]+nums[j]
                k = bisect_left(nums,validVal)
                if k - j - 1 > 0:
                    count += k - j - 1
        return count