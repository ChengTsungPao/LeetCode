lass Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        # 概念: 將有關連的點定義成一個連通圖，此連通圖可以減少到剩一個
        # 方法: 利用DFS上下左右衝
        
        def dfs(x, y):
            if (x, y) in found:
                return 0
            
            found.add((x, y))
            
            count = 1
            for y_ in row[x]:
                count += dfs(x, y_)

            for x_ in col[y]:
                count += dfs(x_, y)
                
            return count
        
        
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        for r, c in stones:
            row[r].append(c)
            col[c].append(r)
        
        ans = 0
        found = set()
        for r, c in stones:
            if (r, c) in found:
                continue
                
            ans += dfs(r, c) - 1
            
        return ans
