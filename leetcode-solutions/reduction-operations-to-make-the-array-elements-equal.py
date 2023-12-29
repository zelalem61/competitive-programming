class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dic = Counter(nums)
        nums.sort(reverse = True)
        count = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                freq = dic[nums[i-1]]
                count+=freq
                dic[nums[i]]+=freq
                del dic[nums[i-1]]
        return count