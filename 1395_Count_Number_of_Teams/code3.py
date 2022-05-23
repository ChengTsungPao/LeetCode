class Solution:
    def numTeams(self, rating: List[int]) -> int:
        from sortedcontainers import SortedList
        
        n = len(rating)
        
        leftSamller = [0] * n
        rightSamller = [0] * n
        
        bst = SortedList([rating[0]])
        for i in range(1, n):
            count = bst.bisect_left(rating[i])
            leftSamller[i] = count
            bst.add(rating[i])
            
        bst = SortedList([rating[-1]])
        for i in range(n - 2, -1, -1):
            count = bst.bisect_left(rating[i])
            rightSamller[i] = count
            bst.add(rating[i])
        
        ans = 0
        for i in range(n):
            leftBiggerCount = i - leftSamller[i]
            rightBiggerCount = (n - i - 1) - rightSamller[i]
            ans += leftSamller[i] * rightBiggerCount + leftBiggerCount * rightSamller[i]

        return ans