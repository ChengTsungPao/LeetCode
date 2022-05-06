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
            
        def divide_and_conquer(cards):
            if len(cards) == 1:
                return [cards[0]]
            
            ans = []
            for i in range(len(cards) - 1):
                for num1 in divide_and_conquer(cards[:i + 1]):
                    for num2 in divide_and_conquer(cards[i + 1:]):
                        ans.append(calculate(num1, num2, "+"))
                        ans.append(calculate(num1, num2, "-"))
                        ans.append(calculate(num1, num2, "*"))
                        ans.append(calculate(num1, num2, "/"))
            return ans
        
        def permutation(cards):
            if not cards:
                return [[]]
            
            ans = []
            for i in range(len(cards)):
                for ret in permutation(cards[:i] + cards[i + 1:]):
                    ans.append([cards[i]] + ret)
            return ans

        for i in range(len(cards)):
            cards[i] = (cards[i], 1)
                    
        for pcards in permutation(cards):
            for a, b in divide_and_conquer(pcards):
                if a == b * 24:
                    return True
            
        return False