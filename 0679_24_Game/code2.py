class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        # 說明: cards的長度只有4，因此不memo
        
        def calculate(num1, num2, symbol):
            a1, b1 = num1
            a2, b2 = num2
            
            if symbol == "+":
                if b1 == b2:
                    ans = (a1 + a2, b1)
                else:
                    ans = (a1 * b2 + a2 * b1, b1 * b2)
            elif symbol == "-":
                if b1 == b2:
                    ans = (a1 - a2, b1)
                else:
                    ans = (a1 * b2 - a2 * b1, b1 * b2)
            elif symbol == "*":
                ans = (a1 * a2, b1 * b2)
            else:
                ans = (a1 * b2, b1 * a2)
                
            if ans[1] == 0 or ans == float("inf"):
                return (float("inf"), 1)
            else:
                return ans
            
        def recur(cards):
            if len(cards) == 1:
                a, b = cards[0]
                return a == b * 24
            
            ans = []
            for i in range(len(cards) - 1):
                for j in range(i + 1, len(cards)):
                    num1 = cards[i]
                    num2 = cards[j]
                    
                    candidates = []
                    candidates.append(calculate(num1, num2, "+"))
                    candidates.append(calculate(num1, num2, "*"))
                    candidates.append(calculate(num1, num2, "-"))
                    candidates.append(calculate(num2, num1, "-"))
                    candidates.append(calculate(num1, num2, "/"))
                    candidates.append(calculate(num2, num1, "/"))
                    
                    for candidate in candidates:
                        if recur([candidate] + cards[:i] + cards[i + 1: j] + cards[j + 1:]):
                            return True
            return False
        
        for i in range(len(cards)):
            cards[i] = (cards[i], 1)
            
        return recur(cards)