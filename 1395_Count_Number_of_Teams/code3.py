class Solution:
    def numTeams(self, rating: List[int]) -> int:
        from sortedcontainers import SortedList
        
        n = len(rating)
        
        leftSamller = [0] * n
        leftBigger = [0] * n
        rightSamller = [0] * n
        rightBigger = [0] * n
        
        bst = SortedList([rating[0]])
        for i in range(1, n):
            count = bst.bisect_left(rating[i])
            leftSamller[i] = count
            leftBigger[i] = len(bst) - count
            bst.add(rating[i])
            
        bst = SortedList([rating[-1]])
        for i in range(n - 2, -1, -1):
            count = bst.bisect_left(rating[i])
            rightSamller[i] = count
            rightBigger[i] = len(bst) - count
            bst.add(rating[i])
        
        ans = 0
        for i in range(n):
            ans += leftSamller[i] * rightBigger[i] + leftBigger[i] * rightSamller[i]

        return ans