class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cal = []
        for n in tokens:
            cal.append(n)
            if cal[-1]=="+" or cal[-1]=="-" or cal[-1]=="*" or cal[-1]=="/":
                cal.append( str(int(eval( str(int(cal[-3])) + cal[-1] + str(int(cal[-2])) ))) )
                del cal[-4:-1]
        return int(cal[0])