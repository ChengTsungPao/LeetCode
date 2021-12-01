class Solution:
    def expand(self, s: str) -> List[str]:
        
        def recur(index):
            
            if index == len(s):
                return [""]

            ans = []
            for ch in sorted(s[index].split(",")):
                for ret in recur(index + 1):
                    ans.append(ch + ret)
                    
            return ans
        
        s = list(filter(lambda element: element != '', re.split("{|}", s.lstrip("{").lstrip("}"))))

        return recur(0)