class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        ans = 0
        stack = []
        
        for attack, defense in sorted(properties, key = lambda x: (x[0], -x[1])):
            while stack and stack[-1] < defense:
                stack.pop()
                ans += 1
                
            stack.append(defense)
            
        return ans