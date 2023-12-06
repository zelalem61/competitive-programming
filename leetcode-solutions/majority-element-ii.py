class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        ans = []
        
        un_nums = set(nums)
        for i in un_nums:
            c = nums.count(i)
            if c > n:
                ans.append(i)
        return ans
        