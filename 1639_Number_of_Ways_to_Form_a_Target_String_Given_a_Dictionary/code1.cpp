class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int numWays(vector<string>& words, string target) {
        unordered_map<int, unordered_map<int, int>> memo;
        return recur(0, 0, target, words, memo);
    }
    
    int recur(int i, int k, string target, vector<string>& words, unordered_map<int, unordered_map<int, int>>& memo){
        
        if(memo[i].find(k) != memo[i].end()){
            return memo[i][k];
        }
        
        if(i >= target.size()){
            return 1;
        } else if (k >= words[0].size()){
            return 0;
        }
        
        int ans = 0;
        for(int j = 0; j < words.size(); j++){
            for(int idx = k; idx < words[j].size(); idx++){
                char ch = words[j][idx];
                if(ch == target[i]){
                    ans += recur(i + 1, idx + 1, target, words, memo) % MOD;
                    ans %= MOD;
                }
            }
        }

        memo[i][k] = ans;
        return ans;
    }
    
};