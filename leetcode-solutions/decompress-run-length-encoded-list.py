class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(0,len(nums),2):
            
            new = [nums[i+1]] * nums[i]
            ans = ans + new
        return ans