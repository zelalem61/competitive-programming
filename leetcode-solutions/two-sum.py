class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = []
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] + nums[j]==target):
                    num.append(j)
                    num.append(i)
                    
        return num            
                