class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        paid = 0
        for i in costs:
            if paid + i <= coins:
                count+=1
                paid+=i
            else:
                break
        return count