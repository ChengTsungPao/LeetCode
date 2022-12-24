class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def getAncestor(a, b):
            if a > b:
                return getAncestor(b, a)
            if a == b:
                return a
            return getAncestor(a, b // 2)
        
        ans = []
        for a, b in queries:
            ancestor = getAncestor(a, b)
            ancestor_h = int(math.log2(ancestor))
            a_h = int(math.log2(a))
            b_h = int(math.log2(b))
            ans.append((a_h - ancestor_h) + (b_h - ancestor_h) + 1)
            
        return ans