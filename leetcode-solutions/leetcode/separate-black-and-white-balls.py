class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        right = len(s)-1
        count = 0
        while left < right:
            if s[left] == "0":
                left += 1
            if s[right] == "1":
                right -= 1
            elif s[left] == "1" and s[right] == "0":
                count += right-left
                right-=1
                left+=1
        return count
            
