class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def validChange(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            return count == 1
        
        def recur(start, visited = set()):
            if start == end:
                return 0
            
            ans = float("inf")
            for s in bank:
                if s in visited or validChange(start, s) == False:
                    continue
                    
                visited.add(s)
                ans = min(ans, recur(s, visited) + 1)
                visited.remove(s)
                
            return ans
        
        ans = recur(start)
        return ans if ans != float("inf") else -1