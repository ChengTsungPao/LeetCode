class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        memo = {}
        
        def recur(left, right):
            
            if (left, right) not in memo:
            
                if left == n and right == n:
                    return [""]
                elif left > n or right > n or right > left:
                    return []

                ans = []
                for ret in recur(left + 1, right):
                    ans.append("(" + ret)
                for ret in recur(left, right + 1):
                    ans.append(")" + ret)
                    
                memo[left, right] = ans
                
            return memo[left, right]
        
        return recur(0, 0)