class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        n= len(nums)
        for i in range (n):
            end = i+1
            while end <= n-1:
                if (nums[i]==nums[end]):
                    output+=1
                end+=1
        return output        
            
            
        