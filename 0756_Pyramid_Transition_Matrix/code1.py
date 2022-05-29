class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:            
            
        n = len(bottom)
        
        statusCharacter = collections.defaultdict(list)
        for left, right, top in allowed:
            statusCharacter[left, right].append(top)
            
        triangle = [[" "] * i for i in range(1, n)]
        triangle.append([bottom[j] for j in range(n)])
        
        memo = set()
        def recur(i, j):
            
            if j > i:
                i -= 1
                j = 0
            
            key = "".join(triangle[i + 1])
            
            if key in memo:
                return False

            if i == -1 and j == 0:
                return True

            left  = triangle[i + 1][j + 0]
            right = triangle[i + 1][j + 1]
                
            for top in statusCharacter[left, right]:

                triangle[i][j] = top
                
                if recur(i, j + 1):
                    return True
                
                triangle[i][j] = ""
            
            if j == 0:
                memo.add(key)
            
            return False

        return recur(n - 2, 0)