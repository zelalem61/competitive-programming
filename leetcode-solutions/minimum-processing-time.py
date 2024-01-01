class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        res = []
        for i in range(len(processorTime)):
            count = 0
            count += processorTime[i]
            count+= max(tasks[i*4:i*4+4])
            res.append(count)
        return max(res)