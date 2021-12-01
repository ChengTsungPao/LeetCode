class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        length = len(tops)
        
        candidate1, candidate2 = tops[0], bottoms[0]
        
        candidate = set([candidate1, candidate2])
        candidate1_count_top, candidate1_count_bottom = 0, 0
        candidate2_count_top, candidate2_count_bottom = 0, 0
        
        for i in range(len(tops)):
            if tops[i] not in candidate and bottoms[i] not in candidate:
                return -1
            
            if tops[i] == candidate1:
                candidate1_count_top += 1
            if bottoms[i] == candidate1:
                candidate1_count_bottom += 1
            if candidate1 in candidate and tops[i] != candidate1 and bottoms[i] != candidate1:
                candidate.remove(candidate1)
        
            if tops[i] == candidate2:
                candidate2_count_top += 1
            if bottoms[i] == candidate2:
                candidate2_count_bottom += 1
            if candidate2 in candidate and tops[i] != candidate2 and bottoms[i] != candidate2:
                candidate.remove(candidate2)
     
        return min(length - candidate1_count_top, length - candidate1_count_bottom, length - candidate2_count_top, length - candidate2_count_bottom)