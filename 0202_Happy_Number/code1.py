class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(num):
            s = 0
            while num > 0:
                s += (num%10)**2
                num //= 10
            return s
        data = set([n])
        while 1==1 :
            n = cal(n)
            if n==1 :
                return True
            elif n in data :
                return False
            else :
                data.add(n)