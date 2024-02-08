class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        count = 0
        prefix = list(accumulate(nums))
        for i in range(len(nums)):
            if (prefix[i] - k) in dic:
                count += dic[prefix[i]-k]
            if prefix[i] in dic:
                dic[prefix[i]] +=1
            else:
                dic[prefix[i]] = 1
        return count