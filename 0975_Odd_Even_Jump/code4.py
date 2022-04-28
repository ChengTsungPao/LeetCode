class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        oddNext = [-1] * n
        evenNext = [-1] * n
        
        stack = []
        for val, index in sorted([(arr[i], i) for i in range(n)]):
            while stack and stack[-1] < index:
                oddNext[stack.pop()] = index
            stack.append(index)
            
        stack = []
        for val, index in sorted([(-arr[i], i) for i in range(n)]):
            while stack and stack[-1] < index:
                evenNext[stack.pop()] = index
            stack.append(index)
            
            
        dpOdd = [False] * n
        dpOdd[n - 1] = True
        dpEven = [False] * n
        dpEven[n - 1] = True

        for index in range(n - 2, -1, -1):            
            evenIndex = oddNext[index]
            oddIndex = evenNext[index]
            
            if evenIndex > 0 and dpEven[evenIndex] == True:
                dpOdd[index] = True
            if oddIndex > 0 and dpOdd[oddIndex] == True:
                dpEven[index] = True
                
        return sum(dpOdd)