class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        m = len(picture)
        n = len(picture[0])
        
        countRow = collections.defaultdict(int)
        countCol = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    countRow[i] += 1
                    countCol[j] += 1
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and countRow[i] == countCol[j] == 1:
                    ans += 1
                    
        return ans