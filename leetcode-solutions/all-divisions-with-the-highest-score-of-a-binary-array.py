class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        sum_ = sum(nums)
        leftSum = 0
        rightSum = sum_
        
        maxDivScore = sum_
        ans = [0]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                leftSum += 1
            else:
                rightSum -= 1
            
            divScore = leftSum + rightSum
            
            if divScore == maxDivScore:
                ans.append(i + 1)
                continue
            if divScore > maxDivScore:
                maxDivScore = divScore
                ans = [i + 1]
                
        return ans