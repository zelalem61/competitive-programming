class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 1
        right = k+1
        res = sum(nums[:k])/k
        current_sum = sum(nums[:k])

        while right <= len(nums):
            current_sum += (nums[right-1] - nums[left-1])
            print(current_sum)
            if current_sum/k > res:
                res = current_sum/k
            left+=1
            right+=1
        return res
        