class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def simplify(equation):
            equation += "+"
            ans = [0, 0]
            s = equation[0]
            for symbol in equation[1:]:
                if symbol == "+" or symbol == "-":
                    if "x" in s:
                        s = s.rstrip("x")
                        s += "1" if s == "" or s == "+" or s == "-" else ""
                        ans[0] += int(s)
                    else:
                        ans[1] += int(s)
                    s = ""
                s += symbol
            return ans
        
        
        left, right = equation.split("=")
        left, right = simplify(left), simplify(right)
        simplify_equation = [left[0] - right[0], left[1] - right[1]]
        
        if simplify_equation[0] != 0:
            ans = "x=" + str(-simplify_equation[1] // simplify_equation[0])   
        elif simplify_equation[1] == 0:
            ans = "Infinite solutions"
        else:
            ans = "No solution"
            
        return ans    