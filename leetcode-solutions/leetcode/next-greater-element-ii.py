class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stack = []
        for i in range(2*len(nums)):
            if i > len(nums)-1:
                i = i - len(nums)
            if len(stack) == 0 or nums[stack[-1]] >= nums[i]:
                stack.append(i) 
            else:
                while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                    ans[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i) 
        return ans
