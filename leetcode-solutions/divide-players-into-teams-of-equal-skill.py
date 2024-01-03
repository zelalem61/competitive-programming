class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill)-1
        sums = skill[i] + skill[j]
        result = 0
        while i < j:
            if skill[i] + skill[j] != sums:
                return -1
            else:
                result = result + (skill[i]*skill[j])
                i += 1
                j -= 1
        return result
            
        
        