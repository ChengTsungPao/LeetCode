class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        ans = 0
        found = {}
        
        i = j = 0
        while j < len(fruits):
            found[fruits[j]] = found.get(fruits[j], 0) + 1
            
            while len(found) > 2:
                found[fruits[i]] -= 1
                if found[fruits[i]] == 0:
                    del found[fruits[i]]
                i += 1
                
            ans = max(ans, j - i + 1)
            j += 1
                
        return ans