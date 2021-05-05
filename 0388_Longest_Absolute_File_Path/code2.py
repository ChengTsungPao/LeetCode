class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        ans, index, stack, stack_total_length, input = 0, 0, [], 0, "\n" + input
        
        while index >= 0:
           
            findindex = input.find("\n", index + 1 , len(input))
            
            count = 0
            while input[index + 1 + count] == "\t":
                count += 1            
            
            while stack and stack[-1][1] >= count:
                stack_total_length -= len(stack[-1][0])
                stack.pop()

            stack.append((input[index + 1 + count : findindex], count))
            stack_total_length += len(stack[-1][0]) + (findindex == -1)

            if stack[-1][0].find(".") != -1:
                ans = max(ans, stack_total_length + len(stack) - 1)

            index = findindex
                    
        return ans