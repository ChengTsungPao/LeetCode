class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        knowledgeDict = {}
        for key, value in knowledge:
            knowledgeDict[key] = value

        ans = word = ""
        isChangeWord = False
        for ch in s:
            if ch == "(":
                isChangeWord = True
            elif isChangeWord and ch == ")":
                ans += knowledgeDict[word] if word in knowledgeDict else "?"
                word = ""
                isChangeWord = False
            elif isChangeWord:
                word += ch
            else:
                ans += ch
                
        return ans