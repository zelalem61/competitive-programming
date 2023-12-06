class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        positive = []
        negative = []
        
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        for j in range(len(positive)):
            ans.append(positive[j])
            ans.append(negative[j])
        return ans
        