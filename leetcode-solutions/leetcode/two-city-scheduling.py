class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_cost = sorted(costs, key=lambda x: x[0] - x[1])
        minimized_cost = 0
        for i in range(len(sorted_cost)):
            if i < len(sorted_cost)//2:
                minimized_cost+=sorted_cost[i][0]
            else:
                minimized_cost+=sorted_cost[i][1]
        return minimized_cost

