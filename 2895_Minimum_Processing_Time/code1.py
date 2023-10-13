class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        n = len(tasks)
        m = len(processorTime)
        
        tasks.sort(reverse = True)
        processorTime.sort()
        
        ans = -float("inf")
        for i in range(m):
            j = 4 * i
            ans = max(ans, processorTime[i] + tasks[j])
            
        return ans