class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            if tickets[i] <= tickets[k] and i <= k:
                res += tickets[i]
            elif tickets[i] > tickets[k] and i < k:
                res += tickets[k]
            elif tickets[i] >= tickets[k] and i > k:
                res += tickets[k] - 1
            elif tickets[i] < tickets[k] and i > k:
                res += tickets[i]
        return res
            