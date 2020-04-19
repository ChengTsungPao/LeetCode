class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if(k==0): return [[]]
        data = []
        for i in  range(1,n+1):
            data.append([i])
        for i in range(k-1):
            tmp = []
            for j in data:
                for k in range(j[-1]+1,n+1):
                    tmp.append(j + [k])
            data = copy.copy(tmp)
        return data