class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M"}
        
        for i in range(3):
            symbol[4 * 10 ** i] = symbol[1 * 10 ** i] + symbol[5 * 10 ** i]
            symbol[9 * 10 ** i] = symbol[1 * 10 ** i] + symbol[1 * 10 ** (i + 1)]
            
        ans = ""
        for n in sorted(symbol.keys(), reverse = True):
            ans += symbol[n] * (num // n)
            num = num % n
        
        return ans