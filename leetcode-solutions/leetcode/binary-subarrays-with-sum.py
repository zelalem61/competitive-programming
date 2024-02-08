class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = {0:1}
        prefix_s = list(accumulate(nums))
        count = 0
        for i in range(len(nums)):
            if (prefix_s[i] - goal) in dic:
                count+=dic[prefix_s[i] - goal]
                if prefix_s[i] not in dic:
                    dic[prefix_s[i]] = 1
                else:
                    dic[prefix_s[i]]+=1
            else:
                if prefix_s[i] in dic:
                    dic[prefix_s[i]]+=1
                else:
                    dic[prefix_s[i]]=1
        return count

