# 同餘證明:
# => (m * a * x + m * b) = (mod * q1 + r1) * x + (mod * q2 + r2) = r1 * x + r2 + mod * constant
# => (m * a * x + m * b) % mod ≡ ((m * a) % mod) * x + ((m * b) % mod)

# 費馬小定理
# =>  a ^ (p - 1) ≡ 1      (mod p) <--- p is prime (10 ** 9 + 7)
# =>  a ^ (p - 2) ≡ a ^ -1 (mod p)
# => (a ^ (p - 2)) * (a * x + b - b) ≡ (a ^ -1) * (a * x + b - b) (mod p)
# => x ≡ (a ^ (p - 2)) * (a * x + b - b) (mod p)
# => x ≡ (a ^ (p - 2)) * (val - b)       (mod p)

# 次方函數說明
# pow(a, m - 2, m) = pow(a, -1, m), when m > 2 in python 3.8

class Fancy:

    def __init__(self):
        self.array = []
        self.a = 1
        self.b = 0
        self.mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self.array.append((val - self.b) * pow(self.a, self.mod - 2, self.mod))
        
    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.mod 
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.array):
            return -1
        return (self.a * self.array[idx] + self.b) % self.mod
            
            

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)