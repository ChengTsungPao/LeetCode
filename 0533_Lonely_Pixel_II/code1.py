class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        
        m = len(picture)
        n = len(picture[0])
        
        rows = [0] * m
        cols = [0] * n
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and rows[i] == cols[j] == target:
                    picture[i][j] = "C"
          
        rowPattern = collections.defaultdict(str)
        for i in range(m):
            rowPattern[i] = "".join(picture[i])

        ans = 0
        for j in range(n):            
            i = 0
            while i < m and picture[i][j] != "C":
                i += 1
            
            pattern = rowPattern[i]
            
            count = 0
            while i < m:
                if picture[i][j] == "C" and pattern == rowPattern[i]:
                    count += 1
                i += 1

            if count == target:
                ans += target
            
        return ans