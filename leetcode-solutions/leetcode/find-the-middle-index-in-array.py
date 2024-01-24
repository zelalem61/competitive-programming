class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_for = list(accumulate(nums))
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if pre_for[-1] - pre_for[i] == 0:
                    return 0
            else:
                if pre_for[i-1] == pre_for[-1] - pre_for[i]:
                    return i
        return -1