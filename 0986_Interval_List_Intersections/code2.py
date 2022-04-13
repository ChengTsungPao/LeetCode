class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        m = len(firstList)
        n = len(secondList)
        
        ans = []
        i = j = 0
        
        while i < m and j < n:
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            start, end = max(start1, start2), min(end1, end2)
            
            if start <= end:
                ans.append([start, end])
                
            if end1 < end2:
                i += 1
            elif end1 > end2:
                j += 1
            else:
                i += 1
                j += 1
                
        return ans