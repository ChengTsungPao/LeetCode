class Solution {
public:
    long long numberOfWays(string s) {
        int n = s.size();
        
        long long ans = 0, dp = 0, dpSumZero = 0, dpSumOne = 0;
        int countOne = 0;
        
        for(int i = 0; i < n; i++){
            dp = (s[i] == '0') ? countOne : i - countOne;
            ans += (s[i] == '0') ? dpSumOne : dpSumZero;
            
            countOne += s[i] == '1';
            dpSumZero += (s[i] == '0') ? dp : 0;
            dpSumOne  += (s[i] == '1') ? dp : 0;
        }
        
        return ans;
    }
};