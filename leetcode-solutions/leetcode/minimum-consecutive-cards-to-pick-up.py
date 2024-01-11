class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        num_dic = {}
        ans = float("inf")
        for index in range(len(cards)):
            if cards[index] not in num_dic:
                num_dic[cards[index]] = index
            else:
                length = index - num_dic[cards[index]] + 1
                ans = min(ans,length)
                num_dic[cards[index]] = index
        if ans == float("inf"):
            return -1
        return ans