class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        n = (num-3) % 3
        
        x = (num-3)//3
      
        
        if n == 0:
            ans.append(x)
            ans.append(x+1)
            ans.append(x+2)
        return ans
     