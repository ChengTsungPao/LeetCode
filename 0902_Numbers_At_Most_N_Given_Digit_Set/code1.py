class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        # Step1: 計算位數較低的所有可能
        # Step2: 計算位數較高的所有可能 => 情況1.高位數相等:下一位需較小 情況2.高位數較小:後面隨意直線排列
        
        n_str = str(n)
        
        count_low_digits = 0
        for i in range(1, len(n_str)):
            count_low_digits += len(digits) ** i
            
        count_same_digits = 0
        for i in range(len(n_str)):
            index = bisect.bisect_left(digits, n_str[i])
            count_same_digits += index * len(digits) ** (len(n_str) - i - 1)
            if not (index < len(digits) and n_str[i] == digits[index]):
                break
            elif i == len(n_str) - 1:
                count_same_digits += 1
                
        return count_low_digits + count_same_digits
        