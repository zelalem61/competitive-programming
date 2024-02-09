class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        query = [0]*len(nums)
        m = 10**9 + 7
        for request in requests:
            start = request[0]
            end = request[1]
            query[start] = query[start]+1
            if end+1 < len(query):
                query[end+1] = query[end+1]-1
        prefix = list(accumulate(query))
        nums.sort()
        prefix.sort()
        res = 0
        for j in range(len(nums)):
            res += nums[j]*prefix[j]
        return res % m