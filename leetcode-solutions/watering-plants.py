class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        c = capacity
        count = 0
        for i in range(len(plants)):
            if c >= plants[i]:
                count += 1
                c -= plants[i]
            else:
                count = count + 2 * (i ) + 1
                c = capacity
                c -= plants[i]
        return count