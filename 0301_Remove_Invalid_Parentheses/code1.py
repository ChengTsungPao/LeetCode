class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        # 先用stack確認可能刪除幾個"("和")"(剪枝)，在進行recur
        
        def recur(index, stack, leftCount, rightCount, memo = {}):
            
            isParentheses = len(stack) == 0 # memo 必須保證先前查找的是Parentheses
            if isParentheses and (index, leftCount, rightCount) in memo:
                return memo[index, leftCount, rightCount] # Parentheses的所有可能

            if leftCount < 0 or rightCount < 0:
                return []
            
            cur_str = ""
            
            if index < len(s):
                while index < len(s) and s[index] != "(" and s[index] != ")":
                    cur_str += s[index]
                    index += 1
                    
            if index == len(s):
                if len(stack) == 0:
                    return [cur_str]
                else:
                    return [] 

            ans = []
            
            # remove
            for _str in recur(index + 1, stack, leftCount - (s[index] == "("), rightCount - (s[index] == ")")):
                ans.append(_str)
            
            # stack => adjust Parentheses
            element = None
            if stack and stack[-1] == "(" and s[index] == ")":
                element = stack.pop()
            else:
                stack.append(s[index])
            
            # add
            for _str in recur(index + 1, stack, leftCount, rightCount):
                ans.append(s[index] + _str)
           
            # backtracking
            if element != None:
                stack.append(element)
            else:
                stack.pop()
            
            # other char
            for i in range(len(ans)):
                ans[i] = cur_str + ans[i]
            
            if isParentheses:
                memo[index, leftCount, rightCount] = ans
            
            return ans
        
        stack = []
        
        for i in range(len(s)):
            
            if s[i] != "(" and s[i] != ")":
                continue
                
            if stack and stack[-1] == "(" and s[i] == ")":
                stack.pop()
            else:
                stack.append(s[i])
                
        count = collections.Counter(stack)
        
        return list(set(recur(0, [], count["("], count[")"])))