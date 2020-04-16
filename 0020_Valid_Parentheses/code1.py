class Solution:
    def isValid(self, s: str) -> bool:
        def same(s1, s2):
            if( (s1=="(" and s2==")") or  (s1==")" and s2=="(") ):
                return False
            elif( (s1=="[" and s2=="]") or  (s1=="]" and s2=="[") ):
                return False
            elif( (s1=="{" and s2=="}") or  (s1=="}" and s2=="{") ):
                return False
            else:
                return True
        stack = []
        for ch in s:
            if(len(stack)==0 or same(stack[-1], ch)):
                stack.append(ch)
            else:
                stack.pop()
        return len(stack)==0