class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        sort_list, n = matrix[0], len(matrix)
        start_index = [i + 1 for i in range(n)]
        
        for i in range(1, n):
            for j in range(n):
                index = bisect.bisect_left(sort_list, matrix[i][j], start_index[j], len(sort_list))
                sort_list.insert(index, matrix[i][j])
                start_index[j] = index + 1
        
        return sort_list[k - 1]