class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        lampSet = set([tuple(lamp) for lamp in lamps])
        
        rowDict = collections.defaultdict(int)
        colDict = collections.defaultdict(int)
        rowRotateDict = collections.defaultdict(int)
        colRotateDict = collections.defaultdict(int)
        
        def rotate(x, y):
            rotatePos = complex(x, y) * complex(1, 1)
            return int(rotatePos.real), int(rotatePos.imag)
        
        def turnoff(i, j):
            for c1 in [-1, 0, 1]:
                for c2 in [-1, 0, 1]:
                    x, y = i + c1, j + c2
                    if (x, y) in lampSet:
                        lampSet.remove((x, y))
                        rowDict[x] -= 1
                        colDict[y] -= 1
                        
                        rx, ry = rotate(x, y)
                        rowRotateDict[rx] -= 1
                        colRotateDict[ry] -= 1
                        
        for x, y in lampSet:
            rowDict[x] += 1
            colDict[y] += 1

            rx, ry = rotate(x, y)
            rowRotateDict[rx] += 1
            colRotateDict[ry] += 1
        
        ans = []
        for x, y in queries:
            rx, ry = rotate(x, y)
            if rowDict[x] > 0 or colDict[y] > 0 or rowRotateDict[rx] > 0 or colRotateDict[ry] > 0:
                ans.append(1)
            else:
                ans.append(0)
                
            turnoff(x, y)
            
        return ans