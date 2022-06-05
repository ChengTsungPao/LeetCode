class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        from sortedcontainers import SortedList
        
        defenseMax = {}
        for attack, defense in properties:
            defenseMax[attack] = max(defenseMax.get(attack, -float("inf")), defense)
        
        bst = SortedList()
        
        ans = 0
        visited = set()
        for attack, defense in sorted(properties, reverse = True):
            
            if attack in visited:
                bst.remove(defenseMax[attack])
                visited.remove(attack)
                
            if len(bst) > 0 and bst.bisect_right(defense) <= len(bst) - 1:
                ans += 1
            
            if defenseMax[attack] not in bst:
                bst.add(defenseMax[attack])
                visited.add(attack)
            
        return ans