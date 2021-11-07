class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # 先記錄每個s的index開始到最後有哪些字母，並儲存其位置
            
        def recur(indexS, indexT, memo = {}):

            if (indexS, indexT) not in memo:
                
                # 若無剪枝 => TLE
                if len(s) - indexS < len(t) - indexT:
                    return 0
                
                if indexT >= len(t):
                    return 1
                if indexS >= len(s):
                    return 0

                memo[indexS, indexT] = 0
                for index in status[indexS][t[indexT]]:
                    memo[indexS, indexT] += recur(index + 1, indexT + 1)

            return memo[indexS, indexT]
        
        status, current = {}, collections.defaultdict(list)
        for i in range(len(s) - 1, -1, -1):
            current[s[i]].append(i)
            status[i] = copy.deepcopy(current)    

        return recur(0, 0)
