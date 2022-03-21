class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        heap = []
        index = [0] * n
        
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i))
        
        for _ in range(k):
            num, i = heapq.heappop(heap)
            index[i] += 1
            if index[i] < n:
                heapq.heappush(heap, (matrix[i][index[i]], i))
            
        return num