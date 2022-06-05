class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        defenseMax = collections.defaultdict(int)
        for attack, defense in properties:
            defenseMax[attack] = max(defenseMax[attack], defense)
            
        suffixDefenseMax = [0] * 100001
        for i in range(100001 - 2, -1, -1):
            suffixDefenseMax[i] = max(suffixDefenseMax[i + 1], defenseMax[i + 1])
        
        ans = 0
        for attack, defense in properties:
            if defense < suffixDefenseMax[attack]:
                ans += 1
            
        return ans