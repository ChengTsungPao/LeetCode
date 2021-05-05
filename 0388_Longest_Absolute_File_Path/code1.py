class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        def recur(path, split_key):
            
            if len(path) == 1:
                return len(path[0])
            
            ans = 0
            for i in range(1, len(path)):
                if path[i].find(".") != -1:
                    ans = max(ans, recur(re.split(split_key + "(?!\t)", path[i]), split_key + "\t"))
                    
            if ans == 0:
                return ans
            else:
                return ans + len(path[0]) + 1
            

        ans = 0
        
        for path in re.split("\n(?!\t)", input):
            if path.find(".") != -1:
                ans = max(ans, recur(re.split("\n\t(?!\t)", path), "\n\t" + "\t"))
                
        return ans