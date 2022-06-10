class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:        
        
        m = len(slots1)
        n = len(slots2)
        
        slots1.sort()
        slots2.sort()
        
        i = j = 0
        while i < m and j < n:
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]
            
            start, end = max([start1, start2]), min([end1, end2])
            if end - start >= duration:
                return [start, start + duration]
            
            if end1 <= end2:
                i += 1
            else:
                j += 1
                
        return []