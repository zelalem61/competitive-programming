class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x < 100:
            if x //10 == x % 10:
                return True
            else:
                return False
        else:
            num = str(x)
            for i in range(len(num)):
                if num[i]==num[-1*(i+1)]:
                    truth= True
                else: 
                    truth= False
                    break
            return truth        
        