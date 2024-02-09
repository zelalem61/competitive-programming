class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {}
        count = 0
        prefix = list(accumulate(nums))
        for i in range(len(nums)):
            if prefix[i] % k in dic:
                count+=dic[prefix[i]%k]
                dic[prefix[i]%k]+=1
                if prefix[i]%k == 0:
                    count+=1
            else:
                if prefix[i]%k == 0:
                    count+=1
                dic[prefix[i]%k] = 1
        print(dic)
        return count
