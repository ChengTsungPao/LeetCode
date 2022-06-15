class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        expressionList = []
        for ch in expression:
            if expressionList and expressionList[-1].isalpha() and ch.isalpha():
                expressionList[-1] += ch
            else:
                expressionList.append(ch)
                
        n = len(expressionList)
        index = [-1] * n

        stack = []
        for i, s in enumerate(expressionList):
            if not (s == "{" or s == "}"):
                index[i] = i
                continue
                
            if stack and stack[-1][1] == "{" and s == "}":
                j, _ = stack.pop()
                index[j] = i
            else:
                stack.append((i, s))

        def mul(left, right):
            if not left or not right:
                return left | right
            return set([l + r  for l in left for r in right])
        
        def recur(i, j):
            if i > j or j >= n:
                return set()
            
            k = index[i]
            left = recur(i + 1, k - 1) if expressionList[i] == "{" else {expressionList[i]}
            
            while k + 1 <= j and expressionList[k + 1] != ",":
                left = mul(left, recur(k + 1, index[k + 1]))
                k = index[k + 1]
            
            right = recur(k + 2, j)
            ans = left | right

            return ans
        
        return sorted(recur(0, n - 1))