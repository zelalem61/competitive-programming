class Solution:
    def totalMoney(self, n: int) -> int:
        num_weeks = n//7
        rem = n%7
        sumOfRem = ((rem/2)*(2*(num_weeks+1) + (rem-1)))
        res = 28*(num_weeks) + (num_weeks/2*(num_weeks - 1)*7) + sumOfRem
        return int(res)
            








            
#         while i < a:
#             for j in range(1,8):
#                 ans+=j+i
#             i+=1