class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def isPowerOfTwo(n):
            return bin(n).count("1") == 1
        
        def permutation(n_string):
            if n_string == "":
                return [""]
            
            ans = []
            for i in range(len(n_string)):
                for ret in permutation(n_string[:i] + n_string[i + 1:]):
                    ans.append(n_string[i] + ret)
                    
            return ans
        
        n_string = str(n)
        for number in permutation(n_string):
            if number[0] != "0" and isPowerOfTwo(int(number)):
                return True
            
        return False