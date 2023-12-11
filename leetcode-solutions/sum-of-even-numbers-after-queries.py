class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic = {}
        a = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                a += nums[i]
                
        for index in range(len(queries)):
            if nums[queries[index][1]] % 2 != 0 and (nums[queries[index][1]] + queries[index][0]) % 2 == 0:
                a = a + nums[queries[index][1]] + queries[index][0]
                ans.append(a)
                nums[queries[index][1]]  = nums[queries[index][1]] + queries[index][0]
            elif nums[queries[index][1]] % 2 == 0 and (nums[queries[index][1]] + queries[index][0]) % 2 == 0:
                a  =  a + queries[index][0]
                ans.append(a)
                nums[queries[index][1]]  = nums[queries[index][1]] + queries[index][0]
            elif nums[queries[index][1]] % 2 == 0 and (nums[queries[index][1]] + queries[index][0]) % 2 != 0:
                a = a - nums[queries[index][1]]
                ans.append(a)
                nums[queries[index][1]]  = nums[queries[index][1]] + queries[index][0]
            elif nums[queries[index][1]] % 2 != 0 and (nums[queries[index][1]] + queries[index][0]) % 2 != 0:
                nums[queries[index][1]]  = nums[queries[index][1]] + queries[index][0]
                ans.append(a)
        if ans == []:
            return [0]
        return ans