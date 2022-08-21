class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        lampSet = set([tuple(lamp) for lamp in lamps])
        
        rowDict = collections.defaultdict(int)
        colDict = collections.defaultdict(int)
        inclineDict1 = collections.defaultdict(int)
        inclineDict2 = collections.defaultdict(int)
        
        def turnoff(i, j):
            for c1 in [-1, 0, 1]:
                for c2 in [-1, 0, 1]:
                    x, y = i + c1, j + c2
                    if (x, y) in lampSet:
                        lampSet.remove((x, y))
                        rowDict[x] -= 1
                        colDict[y] -= 1
                        inclineDict1[x + y] -= 1
                        inclineDict2[x - y] -= 1
                        
        for x, y in lampSet:
            rowDict[x] += 1
            colDict[y] += 1
            inclineDict1[x + y] += 1
            inclineDict2[x - y] += 1
        
        ans = []
        for x, y in queries:
            if rowDict[x] > 0 or colDict[y] > 0 or inclineDict1[x + y] > 0 or inclineDict2[x - y] > 0:
                ans.append(1)
            else:
                ans.append(0)
                
            turnoff(x, y)
            
        return ans