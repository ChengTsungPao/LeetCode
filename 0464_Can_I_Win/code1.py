class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        memo = {}
        def recur(total, bitmask, who):
            
            if bitmask not in memo:
            
                if total <= 0:
                    return not who

                if who:
                    ans = False
                    for i in range(maxChoosableInteger, 0, -1):
                        if bitmask & (1 << i) == 0:
                            ans = ans or recur(total - i, bitmask | (1 << i), not who)
                        if ans: break
                else:
                    ans = True
                    for i in range(maxChoosableInteger, 0, -1):
                        if bitmask & (1 << i) == 0:
                            ans = ans and recur(total - i, bitmask | (1 << i), not who)
                        if not ans: break
                            
                memo[bitmask] = ans if who else not ans
                        
            return memo[bitmask] if who else not memo[bitmask]
        
        if desiredTotal == 0:
            return True
        elif maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        else:
            return recur(desiredTotal, 0, True)