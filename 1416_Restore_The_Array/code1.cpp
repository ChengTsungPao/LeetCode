class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int numberOfArrays(string s, int k) {
        int n = s.size();
        string k_str = to_string(k), curNum(1, s[0]);
        vector<vector<int>> memo(n + 1, vector<int>(10 + 1, -1));
        return recur(1, curNum, s, k_str, memo);
    }
    
    int recur(int idx, string curNum, string& s, string& k_str, vector<vector<int>>& memo) {
        if(curNum[0] == '0' || isBigger(curNum, k_str)){
            return 0;
        } else if (idx >= s.size()){
            return 1;
        }
        
        int curNumLen = curNum.size();
        
        if(memo[idx][curNumLen] != -1){
            return memo[idx][curNumLen];
        }
        
        string digit(1, s[idx]);
        int ans = (recur(idx + 1, curNum + digit, s, k_str, memo) + recur(idx + 1, digit, s, k_str, memo)) % MOD;
        
        memo[idx][curNumLen] = ans;
        return ans;
    }
    
    bool isBigger(string a, string b) {
        if(a.size() != b.size()){
            return a.size() > b.size();
        }
        
        int n = a.size();
        for(int i = 0; i < n; i++){
            if(a[i] != b[i]){
                return a[i] > b[i];
            }
        }
        
        return false;
    }
    
};