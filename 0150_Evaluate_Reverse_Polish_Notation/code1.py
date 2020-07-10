class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if(len(tokens)==1): return int(tokens[0])
        cal = []
        cal.insert(0,tokens.pop())
        cal.insert(0,tokens.pop())
        for _ in range(len(tokens)):
            cal.insert(0,tokens.pop())
            while(len(cal)>=3 and (cal[2]=="+" or cal[2]=="-" or cal[2]=="*" or cal[2]=="/")):
                try:
                    cal.insert(3, str(int(eval( str(int(cal[0])) + cal[2] + str(int(cal[1])) ))) )
                    del cal[:3]
                except:
                    break
        return int(cal[0])