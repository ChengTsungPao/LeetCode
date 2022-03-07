class Solution:
    def canWin(self, currentState: str) -> bool:
        
        def play(currentState):
            index = []
            for i in range(len(currentState) - 1):
                if currentState[i] == currentState[i + 1] == "+":
                    index.append(i)
            return index
        
        memo = {} 
        def recur(currentState, who):
            
            if currentState not in memo:
                index = play(currentState)

                if who:
                    ans = False
                    for i in index:
                        ans = ans or recur(currentState[:i] + "--" + currentState[i + 2:], not who)
                else:
                    ans = True
                    for i in index:
                        ans = ans and recur(currentState[:i] + "--" + currentState[i + 2:], not who)
                        
                memo[currentState] = ans if who else not ans
                    
            return memo[currentState] if who else not memo[currentState]
        
        return recur(currentState, True)