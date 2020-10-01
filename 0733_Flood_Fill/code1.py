class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        def dfs(i, j):
            nonlocal oldColor
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == oldColor:
                image[i][j] = newColor
            else:
                return None
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        if oldColor != newColor:
            dfs(sr, sc)
        return image