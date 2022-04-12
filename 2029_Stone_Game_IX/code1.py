class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        
        '''
        概念: 對於任何情況來說餘數為0的數字，選了之後不會改變任何狀態 (換人的狀態除外)
        分析: 複雜度從O(3^k)降到O(k^2)
        '''
        
        # 統計餘數
        count = {0: 0, 1: 0, 2: 0}
        for stone in stones:
            count[stone % 3] += 1
            
        # 遞迴剪枝
        count[0] = count[0] % 2
            

        def recur(total, count, who):
            
            if total == 0:
                return who            
            elif sum(count.values()) == 0:
                return False

            if who:
                ans = False
                for r in range(3):
                    if count[r] != 0:
                        count[r] -= 1
                        ans = ans or recur((total + r) % 3, count, not who)
                        count[r] += 1
            else:
                ans = True
                for r in range(3):
                    if count[r] != 0:
                        count[r] -= 1
                        ans = ans and recur((total + r) % 3, count, not who)
                        count[r] += 1
                    
            return ans
        
        return recur(3, count, True)
            
            
        
            