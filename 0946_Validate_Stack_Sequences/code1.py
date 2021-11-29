class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # stack permutation、BT 的可能數 => comb(2n, n) / (n + 1)
        
        stack = []
        index = 0
        
        for num in pushed:
            stack.append(num)
            
            while stack and stack[-1] == popped[index]:
                index += 1
                stack.pop()
  
        return len(pushed) == index