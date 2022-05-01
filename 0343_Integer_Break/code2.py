class Solution:
    def integerBreak(self, n: int) -> int:
        
        # Step1 根據算幾不等式，當數字總和固定時，數字越靠近乘積會越大
        # Step2 求極值(x ** (n / x))' = 0 => x = e => 2 < e < 3
        # Step3 由數學歸納法得到2和3所組成的數組乘積較大 => 2*2*2全部換成3*3，接著將3*1換成2*2 (3*3 > 2*2*2 & 2*2 > 3*1)
        
        if n == 2:
            return 1
        elif n == 3:
            return 2
            
        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 2 * 2 * 3 ** (n // 3 - 1)
        else:
            return 2 * 3 ** (n // 3)