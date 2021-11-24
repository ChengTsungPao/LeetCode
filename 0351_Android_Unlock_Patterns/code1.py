class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:            
            
        def isJump(num1, num2):
            pair = set([num1, num2])
            
            if pair == {1, 3} or pair == {4, 6} or pair == {7, 9}:
                return True
            elif pair == {1, 7} or pair == {2, 8} or pair == {3, 9}:
                return True
            elif pair == {1, 9} or pair == {3, 7}:
                return True
            else:
                return False
            
        
        def recur(current, found, memo = {}):
            
            key = str(sorted(found) + [current])
            
            if key not in memo:
            
                if len(found) == k - 1:
                    return 1

                memo[key] = 0

                found.add(current)

                for next_ in range(1, 9 + 1):
                    if next_ in found or (isJump(next_, current) and (next_ + current) // 2 not in found):
                        continue
                    memo[key] += recur(next_, found, memo)

                found.remove(current)
                
            return memo[key]
        
                
        ans = 0
        for k in range(m, n + 1):
            for start in range(1, 9 + 1):
                ans += recur(start, set(), {})
                
        return ans