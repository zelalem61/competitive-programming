class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        ans = 0
        for i in range(len(nums)):
            subSet = set()
            for j in range(i,len(nums)):
                subSet.add(nums[j])
                if len(subSet) == n:
                    ans+=1
        return ans
        