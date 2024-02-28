class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        l=len(nums)
        p=2**(l)
        for i in range(p):
            k=[]
            for j in range(l):
                if i & (1<<j)>0:
                    k.append(nums[j])
            res.append(k)
        return res