class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        dp = set()
        que = collections.deque()
        
        for i in range(len(mat)):        
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    que.appendleft((i, j, 0))
                    dp.add((i, j))
        
        while que:
            i, j, level = que.pop()
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and (x, y) not in dp:
                    mat[x][y] = level + 1
                    que.appendleft((x, y, level + 1))
                    dp.add((x, y))
                
        return mat