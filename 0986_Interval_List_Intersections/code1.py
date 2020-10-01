class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            max_ = max(A[i][0], B[j][0])
            min_ = min(A[i][1], B[j][1])
            if min_ >= max_:
                ans.append([max_, min_])            
            if A[i][1] < B[j][1]:
                i += 1
            else: 
                j += 1
        return ans