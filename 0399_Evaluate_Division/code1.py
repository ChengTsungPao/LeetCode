
class disjoint_set():
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.equation = {}
        
    def findParent(self, s):
        if s not in self.parent:
            return None, None
        
        cur_p, cur_mul = self.parent[s]
        if cur_p == s:
            return s, 1
        
        p, mul = self.findParent(cur_p)
        
        self.equation[s, p] = mul * self.equation[s, cur_p]
        self.parent[s] = (p, self.equation[s, p])
        
        return self.parent[s]
    
    def Uion(self, s1, s2):
        p1, mul1 = self.findParent(s1)
        p2, mul2 = self.findParent(s2)
        
        if p1 == p2:
            return
        
        if self.weight[p1] > self.weight[p2]:
            self.equation[p2, p1] = mul1 * self.equation[s2, s1] / mul2
            self.parent[p2] = (p1, self.equation[p2, p1])
        elif self.weight[p1] < self.weight[p2]:
            self.equation[p1, p2] = mul2 * self.equation[s1, s2] / mul1
            self.parent[p1] = (p2, self.equation[p1, p2])
        else:
            self.equation[p2, p1] = mul1 * self.equation[s2, s1] / mul2
            self.parent[p2] = (p1, self.equation[p2, p1])
            self.weight[p1] += 1
            

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
            
        DIS = disjoint_set()
        
        for i, (a, b) in enumerate(equations):
            DIS.equation[a, b] = 1 / values[i]
            DIS.equation[b, a] = values[i]
            
            if a not in DIS.parent:
                DIS.parent[a] = (a, 1)
                DIS.weight[a] = 0
            if b not in DIS.parent:
                DIS.parent[b] = (b, 1)
                DIS.weight[b] = 0
            
            DIS.Uion(a, b)
        
        ans = []
        for a, b in queries:
            p1, mul1 = DIS.findParent(a)
            p2, mul2 = DIS.findParent(b)
            if p1 == None or p2 == None or p1 != p2:
                ans.append(-1)
            else:
                ans.append(mul2 / mul1)
            
        return ans
