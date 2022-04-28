class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        from sortedcontainers import SortedList
        
        n = len(arr)

        bst = SortedList()
        bst.add(arr[n - 1])
        
        arrIndex = {}
        arrIndex[arr[n - 1]] = n - 1
        
        dpOdd = [False] * n
        dpOdd[n - 1] = True
        dpEven = [False] * n
        dpEven[n - 1] = True

        for index in range(n - 2, -1, -1):
            sortedListLength = n - index - 1
            
            evenIndex = bst.bisect_left(arr[index])
            oddIndex = bst.bisect_right(arr[index]) - 1
                
            evenIndex = arrIndex[bst[evenIndex]] if 0 <= evenIndex < sortedListLength else float("inf")
            oddIndex = arrIndex[bst[oddIndex]] if 0 <= oddIndex < sortedListLength else float("inf")
            
            if evenIndex < n and dpEven[evenIndex] == True:
                dpOdd[index] = True
            if oddIndex < n and dpOdd[oddIndex] == True:
                dpEven[index] = True
                
            bst.add(arr[index])
            arrIndex[arr[index]] = index
        
        return sum(dpOdd)