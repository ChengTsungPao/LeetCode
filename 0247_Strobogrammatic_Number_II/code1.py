class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        # 對稱數組 (0, 0) (1, 1) (6, 9) (8, 8) (9, 6)
        
        pair = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
        
        if n % 2:
            
            arr = ["0","1","8"]
            
            for i in range(1, n, 2):

                tmp = []
                for i in range(len(arr)):
                    for j in range(len(pair)):
                        tmp.append(pair[j][0] + arr[i] + pair[j][1])

                arr = tmp.copy()
                
        else:
            
            arr = ["00","11","69","88","96"]
                
            for i in range(2, n, 2):

                tmp = []
                for i in range(len(arr)):
                    for j in range(len(pair)):
                        tmp.append(pair[j][0] + arr[i] + pair[j][1])

                arr = tmp.copy()

        return arr if n == 1 else filter(lambda number: number[0] != "0", arr)