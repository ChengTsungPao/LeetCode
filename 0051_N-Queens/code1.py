class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        if(n==0):
            return [[]]
        elif(n==1):
            return [["Q"]]
        
        def puzzle(n):
            return [["." for i in range(n)]] + [["k" for i in range(n)] for j in range(n-1)]
        
        def mark(x,y,puzz):
            for i in range(n):
                puzz[i][y] = "."
                puzz[x][i] = "."
            tmpx = x
            tmpy = y
            while(0<=tmpx<n and 0<=tmpy<n):
                puzz[tmpx][tmpy] = "."
                tmpx += 1
                tmpy += 1
            tmpx = x
            tmpy = y
            while(0<=tmpx<n and 0<=tmpy<n):
                puzz[tmpx][tmpy] = "."
                tmpx -= 1
                tmpy -= 1
            tmpx = x
            tmpy = y
            while(0<=tmpx<n and 0<=tmpy<n):
                puzz[tmpx][tmpy] = "."
                tmpx -= 1
                tmpy += 1
            tmpx = x
            tmpy = y
            while(0<=tmpx<n and 0<=tmpy<n):
                puzz[tmpx][tmpy] = "."
                tmpx += 1
                tmpy -= 1
            return puzz

        def dfs(depth):
            nonlocal puzz
            flag = False
            for i in range(n):
                if(puzz[depth][i]=="."):
                    continue
                else:
                    temp = copy.deepcopy(puzz)
                    puzz = mark(depth,i,puzz)
                    puzz[depth][i] = "Q" 
                    flag = True
                if(depth + 1 < n):   
                    dfs(depth + 1)
                    puzz = temp

            if(depth==n-1 and flag):
                for i in range(n):
                    s = ""
                    for j in range(n):
                        s += puzz[i][j]
                    puzz[i] = s
                ans.append(puzz)
        
        tmp = puzzle(n)
        for i in range(n):
            puzz = copy.deepcopy(tmp)
            puzz = mark(0,i,puzz)
            puzz[0][i] = "Q"
            dfs(1)

        return ans
        