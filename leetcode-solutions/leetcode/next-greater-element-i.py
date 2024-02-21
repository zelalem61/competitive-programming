class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        res = []
        for i in range(len(nums2)):
            if not stack or nums2[stack[-1]] >= nums2[i]:
                stack.append(i)
            else:
                while stack and nums2[stack[-1]] < nums2[i]:
                    index = stack.pop()
                    dic[nums2[index]] = nums2[i]
                stack.append(i)
        for num in nums1:
            if num not in dic:
                res.append(-1)
            else:
                res.append(dic[num])
        return res
        
        
            
