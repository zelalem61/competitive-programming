class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        new  = 0
        for i in range(len(nums)):

            if nums[i] == 1:
                new += 1
            
            else:
                if new > count:
                    count = new
                new = 0
        if new > count:
            count = new
            
        return count