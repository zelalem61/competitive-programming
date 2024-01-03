class Solution:
     def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        n = len(people)
        check = set()
        res = 0
        for i in range(n-1,-1,-1):
            if i in check:
                continue
            res += 1
            check.add(i)
            x = people[i]
            cap = limit - x
            l,r = 0,i-1
            while l<=r: # binary search to find the heaviest pairing within limit
                m = l+(r-l)//2
                if people[m] <= cap:
                    l = m+1
                else:
                    r = m-1
            if not r in check: # -1 can be added to check as well
                check.add(r)
            else:
                while r>=0 and r in check: # worest case O(n)
                    r -= 1
                if r>=0:
                    check.add(r)
        return res


        