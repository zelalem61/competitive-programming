class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        jungle = {}
        count = 0
        for ans in answers:
            if ans not in jungle:
                count+=ans+1
                if ans != 0:
                    jungle[ans] = ans
            else:
                jungle[ans]-=1
                if jungle[ans] == 0:
                    del jungle[ans]
        return count