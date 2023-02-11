class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        n = len(board)
        
        def get_remove_range(idx, board):
            l = r = idx
            while l >= 0 and r < len(board):
                color = board[l]
                count = -1 if l == r else 0
                next_l, next_r = l, r
                while next_l >= 0 and board[next_l] == color:
                    next_l -= 1
                    count += 1
                while next_r < len(board) and board[next_r] == color:
                    next_r += 1
                    count += 1
                if count < 3:
                    break
                l, r = next_l, next_r
            return (l, r) if l != r else (idx, idx + 1) 
        
        @functools.lru_cache(None)
        def recur(board, hand):
            if board == "":
                return 0
            elif hand == "":
                return float("inf")
            
            ans = float("inf")
            for i in range(len(board) + 1):
                for j, color in enumerate(hand):
                    if j > 0 and hand[j - 1] == hand[j]:
                        continue
                        
                    # case 1 => same "W" insert "WW" => "(W)WW" == "W(W)W" == "WW(W)"
                    if i < len(board) and board[i] == color:
                        continue
                        
                    # case 2 => diff "R" split "WW" => "W(R)W"
                    if 0 < i < len(board) and board[i] != color and board[i - 1] != color and board[i] != board[i - 1]:
                        continue
                        
                    newBoard = board[:i] + color + board[i:]
                    l, r = get_remove_range(i, newBoard)
                    newBoard = newBoard[:l + 1] + newBoard[r:]
                    newHand = hand[:j] + hand[j + 1:]
                    
                    ans = min(ans, 1 + recur(newBoard, newHand))
                    
            return ans
        
        
        hand = "".join(sorted(hand))
        ans = recur(board, hand)
        return ans if ans != float("inf") else -1