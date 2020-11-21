class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        for i in range(len(paths)):
            start.add(paths[i][0])
        for i in range(len(paths)):
            if paths[i][1] not in start:
                return paths[i][1]