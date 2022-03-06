class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        # total[i] => 0 到 i-1可旋轉數字的數量
        # canRotate[i] => 0 到 i-1旋轉後不變數字的數量
        total     = [0, 1, 2, 3, 3, 3, 4, 5, 5, 6]
        canRotate = [0, 1, 2, 2, 2, 2, 2, 2, 2, 3]
        
        # 需+1避免少算最後一個
        n = str(n + 1)
        number_length = len(n)
        validDigit = set([0, 1, 8, 2, 5, 6, 9])
        canRotateDigit = set([0, 1, 8])
        
        # 計算可旋轉的組合
        valid_count = 0
        for i in range(number_length):
            digit = int(n[i])
            valid_count += total[digit] * 7 ** (number_length - i - 1)
            if digit not in validDigit:
                break
                
        # 計算旋轉後不變的組合
        canRotate_count = 0
        for i in range(number_length):
            digit = int(n[i])
            canRotate_count += canRotate[digit] * 3 ** (number_length - i - 1)
            if digit not in canRotateDigit:
                break        
            
        return valid_count - canRotate_count