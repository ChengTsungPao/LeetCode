class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        ans = []
        count = collections.Counter(changed)
        
        for num in sorted(changed):
            if count[num] == 0:
                continue
            
            if count[num * 2] > 0 and (num != 0 or count[num] >= 2):
                ans.append(num)
                count[num] -= 1
                count[num * 2] -= 1
            else:
                return []
                
        return ans