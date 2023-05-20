class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Floyd Warshall
        
        var_set = set()
        equations_dict = {}
        for (a, b), val in zip(equations, values):
            equations_dict[a, b] = val
            equations_dict[a, a] = 1
            equations_dict[b, b] = 1
            var_set |= {a, b}
        
        for c in var_set:
            for a in var_set:
                for b in var_set:
                    if (a, c) in equations_dict and (c, b) in equations_dict:
                        equations_dict[a, b] = equations_dict[a, c] * equations_dict[c, b]
                        equations_dict[b, a] = 1 / equations_dict[a, b]
                        
        ans = []
        for a, b in queries:
            if (a, b) not in equations_dict:
                ans.append(-1)
            else:
                ans.append(equations_dict[a, b])
                
        return ans