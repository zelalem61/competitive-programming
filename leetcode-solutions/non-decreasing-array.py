class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        
        for i in range(len(nums)-1):
            if nums[i+1] >= nums[i]:
                continue
            else:
                if nums[i+2:] != sorted(nums[i+2:]):
                    count+=1
                    return False
                elif i == 0:
                    count += 1
                elif nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                    count+=1
                elif nums[i+1] >= nums[i-1]:
                    nums[i] = nums[i+1]
                    count+=1
        if count <= 1:
            return True
        elif count > 1:
            return False