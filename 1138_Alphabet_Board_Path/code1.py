class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        position = {}
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                position[board[i][j]] = (i, j)
        
        
        ans = ""
        preCh = "a"
        
        for ch in target:
            i, j = position[preCh]
            i_, j_ = position[ch]
            
            if i_ > i:
                row = (i_ - i) * "D"
            else:
                row = (i - i_) * "U"
                
            if j_ > j:
                col = (j_ - j) * "R"
            else:
                col = (j - j_) * "L"
            
            if preCh == "z":
                ans += row + col + "!"
            else:
                ans += col + row + "!"
                
            preCh = ch
            
        return ans