class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_of_nums = sum(cardPoints)
        left = 0
        right = 0
        min_sum = float("inf")
        k_subArraySum = 0
        if len(cardPoints) - k == 0:
            return sum_of_nums
        while right < len(cardPoints):
            if right - left < len(cardPoints)-k:
                k_subArraySum += cardPoints[right]
            else:
                print(min_sum)                           
                min_sum = min(min_sum,k_subArraySum)      
                k_subArraySum -= cardPoints[left]
                k_subArraySum += cardPoints[right]
                left+=1
            right+=1
        min_sum = min(min_sum,k_subArraySum)    
        return sum_of_nums - min_sum


