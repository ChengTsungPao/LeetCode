class Solution:
    def knightDialer(self, n: int) -> int:
        
        def getPosition(digit):
            if digit == 0:
                return 3, 1
            else:
                return (digit - 1) // 3, (digit - 1) % 3
            
        def getNextCountTable(countTable):
            nextCountTable = [[0] * 3 for _ in range(4)]
            for i in range(4):
                for j in range(3):
                    for digit in nextState[i][j]:
                        i_, j_ =  getPosition(digit)
                        nextCountTable[i_][j_] += countTable[i][j]
            return nextCountTable
        
        # 每個數字下一個可能訪問的數字
        nextState = [
            [[   6, 8], [7, 9], [   4, 8]],
            [[0, 3, 9], [    ], [0, 1, 7]],
            [[   2, 6], [1, 3], [   2, 4]],
            [[       ], [4, 6], [        ]]
        ]  
        
        # 訪問n次後，每個數字最終被訪問的次數
        countTable = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 0]
        ]
        
        # 利用前一次的countTable計算當前的countTable
        for _ in range(1, n):
            countTable = getNextCountTable(countTable)
        
        ans = 0
        for i in range(4):
            for j in range(3):
                ans += countTable[i][j]
                    
        return ans % (10 ** 9 + 7)