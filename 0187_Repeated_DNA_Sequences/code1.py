class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n = len(s)
        if n < 10:
            return []
        
        ans = set()
        curString = s[:10]
        visited = set([curString])
        for index in range(10, n):
            curString = curString[1:] + s[index]
            if curString in visited:
                ans.add(curString)
            visited.add(curString)
                
        return list(ans)