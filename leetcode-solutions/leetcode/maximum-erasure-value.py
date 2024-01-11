class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        summ = 0
        ans = 0
        dic = {}
        for right in range(len(nums)):
            if nums[right] not in dic:
                dic[nums[right]] = right
                summ+=nums[right]
                ans = max(ans,summ)
            else:
                summ+=nums[right]
                index = dic[nums[right]]
                dic[nums[right]] = right
                if index >= left:
                    add = sum(nums[left:index+1])
                    summ-=add
                    left = index+1
                ans = max(ans,summ)
               
                

        return ans


