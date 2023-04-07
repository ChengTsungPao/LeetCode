class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        
        s.push_back('0');
        
        char preCh;
        int ans = 0;
        int countZeros = 0, countOnes = 0;
        for(char ch: s){
            if(ch == '0'){
                ans = max(ans, min(countZeros, countOnes) * 2);
                countZeros += 1;
                countOnes = 0;
                if(preCh == '1') countZeros = 1;
            } else {
                countOnes += 1;
            }
            preCh = ch;
        }
        
        return ans;
    }
};