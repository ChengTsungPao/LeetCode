class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = []
        
        def recur(head):
            if head > n:
                return
            
            ans.append(head)

            for d in range(10):
                if head * 10 + d <= n:
                    recur(head * 10 + d)
                else:
                    break
        
        for d in range(1, 10):  
            recur(d)
            
        return ans