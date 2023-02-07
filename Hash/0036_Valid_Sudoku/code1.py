class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        i_set = [set() for _ in range(9)]
        j_set = [set() for _ in range(9)]
        s_set = [set() for _ in range(9)]
        
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                if ch == ".":
                    continue
                
                s_idx = (i // 3) * 3 + (j // 3)
                if ch in i_set[i] or ch in j_set[j] or ch in s_set[s_idx]:
                    return False
                
                i_set[i].add(ch)
                j_set[j].add(ch)
                s_set[s_idx].add(ch)
                
        return True