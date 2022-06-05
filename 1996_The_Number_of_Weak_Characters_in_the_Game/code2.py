class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        ans = 0
        preAttack = preDefense = 0
        maxDefense = -float("inf")
        
        for attack, defense in sorted(properties, key = lambda x: (-x[0], x[1])):
            
            if attack != preAttack:
                maxDefense = max(maxDefense, preDefense)
                
            if defense < maxDefense:
                ans += 1
                
            preAttack, preDefense = attack, defense
            
        return ans