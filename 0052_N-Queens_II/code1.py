class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        if(n==0):
            return 0
        elif(n==1):
            return 1
        
        def dfs(depth,pos):
            nonlocal ans
            finalflag = False
            for i in range(n):
                flag = False
                for q in pos:
                    if(q%n==i or abs(q//n-depth)==abs(q%n-i)):
                        flag = True
                        break
                if(flag):
                    continue
                else:
                    finalflag = True
                if(depth + 1 < n):   
                    dfs(depth+1,pos+[depth*n+i])
            if(depth==n-1 and finalflag):
                ans += 1

        pos = []
        for i in range(n):
            dfs(1,pos+[0*n+i])

        return ans