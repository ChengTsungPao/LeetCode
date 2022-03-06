class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        ans = []
        isComment = False
        code = ""
        
        for lineString in source:
            
            i = 0
            while i < len(lineString):
                if isComment:
                    if lineString[i: i + 2] == "*/":
                        isComment = False
                        i += 1
                else:
                    if lineString[i: i + 2] == "//":
                        break
                    elif lineString[i: i + 2] == "/*":
                        isComment = True
                        i += 1
                    else:
                        code += lineString[i]
                i += 1
                        
            if isComment == False and len(code) > 0:
                ans.append(code)
                code = ""
                        
        return ans