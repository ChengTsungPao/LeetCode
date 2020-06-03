class Solution:
    def solve(self, board: List[List[str]]) -> None:
        mark = copy.deepcopy(board)
        
        def dfs1(x, y):  
            if(board[x][y]=="X" or board[x][y]=="Q"):
                return
            board[x][y] = "Q"
            if(x==len(board)-1 or y==len(board[0])-1 or x==0 or y==0):
                return True 
            if(dfs1(x+1, y)):
                return True
            if(dfs1(x, y+1)):
                return True
            if(dfs1(x-1, y)):
                return True
            if(dfs1(x, y-1)):
                return True
            
        def dfs2(x, y):
            nonlocal ch 
            if(x==len(board) or y==len(board[0]) or x==-1 or y==-1 or board[x][y]=="X" or board[x][y]==ch):
                return
            else:
                board[x][y] = ch
                mark[x][y] = "X"
            dfs2(x+1, y)
            dfs2(x, y+1)
            dfs2(x-1, y)
            dfs2(x, y-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(mark[i][j]=="O"):
                    if(dfs1(i, j)):
                        ch = "O"
                    else:
                        ch = "X"
                    dfs2(i, j)