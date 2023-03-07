class Solution {
public:
    vector<int> divisibilityArray(string word, int m) {
        /*
        "998244353", m = 3
         9 % m = 0
         (0 * 10 + 9) % m = 0
         (0 * 10 + 8) % m = 2
         (2 * 10 + 2) % m = 1
         ...
         
        */
        
        vector<int> ans;
        long long curNum = 0;
        
        for(char ch: word){
            curNum *= 10;
            curNum += ch - '0';
            curNum %= m;
            ans.push_back((curNum == 0) ? 1 : 0);
        }
        
        return ans;
    }
};