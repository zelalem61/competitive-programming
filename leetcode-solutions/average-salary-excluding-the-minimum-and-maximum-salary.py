class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        return mean(salary[1:n-1])
        