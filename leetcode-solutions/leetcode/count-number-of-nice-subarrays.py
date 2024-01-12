class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd_indeces = []
        count = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_indeces.append(right)
            if len(odd_indeces) > k:
                left = odd_indeces[0] + 1
                del odd_indeces[0]
            if len(odd_indeces) == k:
                count += odd_indeces[0] - left + 1
        return count
            

