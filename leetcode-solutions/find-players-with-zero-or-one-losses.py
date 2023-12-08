class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers_dic = {}
        ans =[]
        for players in matches:
            if players[1] not in losers_dic:
                losers_dic[players[1]] = 1
            else:
                losers_dic[players[1]]+=1
        winners_with_no_lose = []
        for pl in matches:
            if pl[0] not in losers_dic and pl[0] not in winners_with_no_lose:
                winners_with_no_lose.append(pl[0])
        losers_exactly_one_lose =[]
        for key in losers_dic:
            if losers_dic[key] == 1:
                losers_exactly_one_lose.append(key)
        winners_with_no_lose.sort()
        losers_exactly_one_lose.sort()
        ans.append(winners_with_no_lose)
        ans.append(losers_exactly_one_lose)
        return ans