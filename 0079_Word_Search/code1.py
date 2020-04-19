class Solution:
    def init(self):
        self.map = []
    def exist(self, board: List[List[str]], word: str) -> bool:
        import numpy as np
        if(len(board)==0 and len(board[0])==0): 
            return False
        elif(len(board)==1 and len(board[0])==1): 
            if(word==board[0][0]):
                return True
            else:
                return False

        def recur(s,x,y):
            if(len(s)!=1):
                if(y+1<len(board[0])):
                    if(board[x][y+1]==s[1] and self.map[x][y+1]==1):
                        self.map[x][y+1]=0
                        if(recur(s[1:],x,y+1)):
                            return True
                        self.map[x][y+1]=1
                if(x+1<len(board)):
                    if(board[x+1][y]==s[1] and self.map[x+1][y]==1):
                        self.map[x+1][y]=0
                        if(recur(s[1:],x+1,y)):
                            return True
                        self.map[x+1][y]=1
                if(x-1>=0):
                    if(board[x-1][y]==s[1] and self.map[x-1][y]==1):
                        self.map[x-1][y]=0
                        if(recur(s[1:],x-1,y)):
                            return True
                        self.map[x-1][y]=1
                if(y-1>=0):
                    if(board[x][y-1]==s[1] and self.map[x][y-1]==1):
                        self.map[x][y-1]=0
                        if(recur(s[1:],x,y-1)):
                            return True
                        self.map[x][y-1]=1
            else:
                return True    
              
        for i in range(len(board)):
            for j in range(len(board[0])): 
                if(board[i][j]==word[0]):
                    self.map = np.ones((len(board),len(board[0])))  
                    self.map[i][j] = 0
                    if(recur(word,i,j)): return True
        return False