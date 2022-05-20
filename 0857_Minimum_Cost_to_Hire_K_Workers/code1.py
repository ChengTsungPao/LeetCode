class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        from sortedcontainers import SortedList
        
        sorted_arr = sorted(zip(quality, wage), key = lambda x: (x[1] / x[0], x[1]))
        n = len(sorted_arr)

        bst = SortedList()
        
        qSum = 0
        for i in range(k - 1):
            q, w = sorted_arr[i]
            bst.add(q)
            qSum += q
            
        ans = float("inf")    
        for i in range(k - 1, n):
            q, w = sorted_arr[i]
            ans = min(ans, (w / q) * (qSum + q))
            
            qSum += q
            bst.add(q)
            
            qSum -= bst[-1]
            bst.remove(bst[-1])
            
        return ans