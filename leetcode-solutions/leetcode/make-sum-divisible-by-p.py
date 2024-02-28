class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        cur_sum = sum(nums)
        if cur_sum < p:
            return -1
        if 0 == cur_sum % p:
            return 0
        prefix = 0
        subs = {0: 0}
        out = len(nums)
        for index, val in enumerate(nums):
            prefix += val
            sub = (prefix - cur_sum) % p
            if sub in subs:
                out = min(out, (index + 1 - subs[sub]))
            subs[prefix % p] = index + 1  
        return out if out < len(nums) else -1