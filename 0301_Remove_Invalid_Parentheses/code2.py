class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(_str):
            stack = []
            for s in _str:
                if s != "(" and s != ")":
                    continue
                if stack and stack[-1] == "(" and s == ")":
                    stack.pop()
                else:
                    stack.append(s)
            return len(stack) == 0
        
        
        que = collections.deque()
        que.appendleft(s)
        
        ans = set()
        maxlength = 0
        found = set()
        
        while que:
            _str = que.pop()
            
            if len(ans) > 0 and len(_str) < maxlength:
                continue
            elif isValid(_str):
                maxlength = max(maxlength, len(_str))
                ans.add(_str)
                continue
                
            for i in range(len(_str)):
                if _str[i] != "(" and _str[i] != ")":
                    continue
                _s = _str[:i] + _str[i + 1:]
                if _s not in found:
                    que.appendleft(_s)
                    found.add(_s)
                
        return ans
