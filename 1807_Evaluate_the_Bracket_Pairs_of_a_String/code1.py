class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        knowledgeDict = {}
        for key, value in knowledge:
            knowledgeDict[key] = value
            
        def findPair(s):
            ret = []
            for i, ch in enumerate(s):
                if ch == "(":
                    ret.append([i])
                elif ch == ")":
                    ret[-1].append(i)
            return ret
        
        n = len(s)
        for i, j in reversed(findPair(s)):
            changeWord = knowledgeDict[s[i + 1: j]] if s[i + 1: j] in knowledgeDict else "?"
            s = s[:i] + changeWord + s[j + 1:]
            
        return s