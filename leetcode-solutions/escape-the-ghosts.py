class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d = []
        
        for i in range(len(ghosts)):
            a = abs(target[0]- ghosts[i][0]) + abs(target[1]-ghosts[i][1])
            d.append(a)
        closest = min(d)
        goalD = abs(target[0]) + abs(target[1])
        if goalD < closest:
            return True
        else:
            return False