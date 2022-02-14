class Codec:
    def create_table(self, strs):
        char = set("".join(strs))
        
        self.encode_table = {}
        self.decode_table = {}
        
        for ch, num in zip(char, random.sample(range(len(char) * 10), len(char))):
            self.encode_table[ch] = num            
            self.decode_table[num] = ch
            
    
    def encode(self, strs: [str]) -> str:
        self.create_table(strs)
        
        ans = []
        for str_ in strs:
            ans.append("")
            for ch in str_:
                ans[-1] += str(self.encode_table[ch]) + "#"
            ans[-1] = ans[-1][:-1]
        return ans
    

    def decode(self, s: str) -> [str]:
        ans = []
        for str_ in s:
            ans.append("")
            if str_ == "":
                continue
            for ch in str_.split("#"):
                ans[-1] += self.decode_table[int(ch)]
        return ans
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))